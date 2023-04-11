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

2. Then rename both .env.template file to .env file. inside `payment-search-tool-api` & `payment-search-tool-ui` directory by running it.
```bash
    cp payment-search-tool-api/.env.template payment-search-tool-api/.env && cp payment-search-tool-ui/.env.template payment-search-tool-ui/.env
```

3. Now to start both backend and front end application.
```bash
    docker compose up -d --build
```

4. Then Data needs to be Inserted First.
```bash
    docker exec $(docker ps --filter "name=reorg-case-study-be_app" --format "{{.ID}}") sh -c 'python insert_data.py'
```

5. As insertion time depends on amount of Data, meanwhile you can open [http://localhost:3000](http://localhost:3000) to view it in your browser.

Update payment data if required
```bash
    docker exec $(docker ps --filter "name=reorg-case-study-be_app" --format "{{.ID}}") sh -c 'python update_data.py'
```

---
**NOTE**

If it's for Production Deployment, I would have considered any of the following course of actions: 
- Elasticsearch'd be an excellent choice for implementing the search functionality. Real-time search with auto-completion and fuzzy matching, which are great for implementing typeahead functionality. 

- Choosing MongoDB as its database is a valid option. Having said that, it may not be the best choice for production site if data heavily rely on complex relational queries or ACID transactions for production site. So understanding the data & its relation are key factor to choose which I avoided due the time constraints.

- Initially, I did consider pyspark because of its large volumes of data and support distributed processing capabilities. For case study, it might be bit-exorbitant.

- Current strategies of RDBMS-db/table can be used for raw purpose. Once getting familiar with the data and its relation, we'll have another db/table for production where relationships between different entities and model are well defined and structured to ensure data consistency and integrity.

*Because of time constraints and the nature/purpose of case-study, I've just kept it very simple.

---