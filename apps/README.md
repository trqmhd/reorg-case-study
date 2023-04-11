## Getting Started

This project contains both backend and frontend application to Open Payment Search Tool

### Prerequisites

Kindly ensure you have the following installed:
- Docker

### Project Structure

```
├── README.md
├── docker-compose.yml
├── dockerfiles
│   ├── backend.dockerfile
│   ├── frontend.dockerfile
│   └── nginx.dockerfile
├── nginx.conf
├── payment-search-tool-api
│   ├── README.md
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── get_data.py
│   ├── model.py
│   ├── requirements.txt
│   ├── route
│   │   ├── export.py
│   │   ├── search.py
│   │   └── typeahead.py
│   ├── static
│   │   └── index.html
│   ├── test
│   │   ├── __init__.py
│   │   └── test_typeahead.py
│   ├── update_data.py
│   ├── utils.py
└── payment-search-tool-ui
    ├── README.md
    ├── next-env.d.ts
    ├── next.config.js
    ├── node_modules
    ├── package.json
    ├── postcss.config.js
    ├── public
    │   ├── favicon.ico
    │   ├── next.svg
    │   └── vercel.svg
    ├── src
    │   ├── components
    │   ├── pages
    │   ├── styles
    │   └── utils
    ├── tailwind.config.js
    ├── tsconfig.jso
```


### How to Run

1. Clone the Repository

2. Then rename both .env.template file to .env file. inside `payment-search-tool-api` & `payment-search-tool-ui` directory. 
```bash
    cat .env.example > .env
```
then change following database uri with vallues

```bash
    LOCAL_SQLALCHEMY_DATABASE_URI='mysql+pymysql://<MYSQL_USER>:<MYSQL_PASSWORD>@db/<MYSQL_DATABASE>'
    MYSQL_DATABASE=<XXXXX>
    MYSQL_USER=<XXXXX>
    MYSQL_PASSWORD=<XXXXX>
    MYSQL_ROOT_PASSWORD=<XXXXX> 
```

3. Now to start both backend and front end application.
```bash
    docker compose up -d --build --remove-orphans
```

4. Then Data needs to be Inserted First.
```bash
    docker exec <CONTAINER_ID_BE_APP> sh -c 'python insert_data.py'`
```
    *you can get container id by running `docker ps` command

5. As insertion time depends on amount of Data, meanwhile you can open [http://localhost:3000](http://localhost:3000) to view it in your browser.

Update payment data if required
```bash
    docker exec <CONTAINER_ID_BE_APP> sh -c 'python update_data.py'`
```