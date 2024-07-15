# script for writing vars from .env to .env.template for increased security

if __name__ == "__main__":
    with open('.env', 'r') as source_file:
        with open('.env.template', 'w') as dest_file:
            for line in source_file:
                if '=' in line:
                    key = line.split('=')[0]
                    dest_file.write(key + '=\n')
                else:
                    dest_file.write(line)
