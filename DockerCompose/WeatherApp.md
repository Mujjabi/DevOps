# The Weather App
These are notes for 

# Data Base
Redis db
- collecting cache from user - in-session caching. When user behavior is stored to enhance user convenience. Like when you google something, next time, Google will give you suggestions based on your history of searches.
- When I watch the Premier League, YouTube will suggest other Premier League matches without searching them.

DB
- this stores information and can be recovered by the user if asked. For example, login information can be stored on here. 


## Connection Strings
AUTH HOST= auth
AUTH _PORT=8080
WEATHER HOST= weather
WEATHER PORT= 5000
REDIS USER=redis
REDIS PASSWORD=redis
- these are environmental variables. password etc


db:
    container_name: thomosis-db
    image: devopseasylearning/thomosis-db:v0.0.1
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
    volumes:
      - db-data:/var/lib/mysql
    networks:
      - thomisis
    restart: always


    redis:
    container_name: thomosis-redis
    image: redis
    networks:
      - thomisis
    environment:
      - REDIS_USER=redis
      - REDIS_PASSWORD=redis
    restart: always



    ## 
    docker login -u devopseasylearning -p dckr_pat_e_n214_A6_fX1p8q9nNFmsIQkvA

    clone from prince
    git@github.com:PrinceDalton/Begin.Practice.git
