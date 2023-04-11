# Specify the base image
FROM node:16-alpine

# Set the working directory
WORKDIR /frontend-app

# Copy the package.json and package-lock.json files
COPY ./payment-search-tool-ui/package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application code
COPY ./payment-search-tool-ui/. .

# # Build the Next.js app
# RUN yarn build

# Expose port 3000
EXPOSE 3000

# Specify the command to run when the container starts
CMD ["yarn", "dev"]
