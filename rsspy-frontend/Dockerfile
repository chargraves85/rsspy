FROM node:14
# Set working directory
WORKDIR /app
RUN npm install -g gatsby-cli; apt-get update; apt-get -y install libvips
# Copy all files from current directory to working dir in image
COPY . .
# install node modules and build assets
RUN yarn install && yarn build
