# nginx state for serving content
FROM nginx:alpine
# Set working directory to nginx asset directory
COPY nginx.conf /etc/nginx/nginx.conf
# Containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]