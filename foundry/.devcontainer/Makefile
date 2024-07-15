################################################
#
# go mod commands
#
################################################

# tidy go modules && get missing ones
tidy:
	cd .. \
	&& go mod tidy \
	&& cd -

################################################
#
# docker commands
#
################################################

# build devcontainer image
build:
	docker build -t devcontainer -f Dockerfile ..

buildnc:
	docker build --no-cache -t devcontainer -f Dockerfile ..
