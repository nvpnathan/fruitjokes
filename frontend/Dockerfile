FROM public.ecr.aws/docker/library/node:18 AS build

MAINTAINER nvpnathan

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# Second stage build
FROM public.ecr.aws/docker/library/node:18-slim

COPY --from=build /app .

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]
