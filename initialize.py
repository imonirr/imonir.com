#!/usr/bin/env python3.6

#  from subprocess import call
from pathlib import Path
#  import sys
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


PROJECT_NAME = 'imonir'
ENVIRONMENT = Path('.env.run').read_text().rstrip()

print(f"Environment: {ENVIRONMENT}")
notDevelopment = ENVIRONMENT != 'development'


# CONTAINERS

# env vars
nodeEnv = ENVIRONMENT


# front env vars
virtualHostFront = 'www.imonir.com' if notDevelopment  else 'local.www.imonir.com'
virtualPortFront = 4100


# back env vars
virtualHostBack = 'api.imonir.com' if notDevelopment  else 'local.api.imonir.com'
virtualPortBack = 8100
jwtSecret = id_generator(32)
corsOrigin = virtualHostFront
#  fbClientId = process.env.FACEBOOK_CLIENTID,
#  fbClientSecret = process.env.FACEBOOK_CLIENTSECRET,

apiUrl = virtualHostBack
apiUrlFromServer = 'imonir_back'


# front env file
envContainerFront = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}\n\n"\
      f"VIRTUAL_HOST={virtualHostFront}\n"\
      f"VIRTUAL_PORT={virtualPortFront}"

# back env file
envContainerBack = f"COMPOSE_PROJECT_NAME={PROJECT_NAME}\n\n"\
      f"VIRTUAL_HOST={virtualHostBack}\n"\
      f"VIRTUAL_PORT={virtualPortBack}"


envFrontend = f"NODE_ENV={nodeEnv}\n\n"\
      f"PORT={virtualPortFront}\n"\
      f"API_URL={apiUrl}:{virtualPortBack}\n"\
      f"API_URL_FROM_SERVER={apiUrlFromServer}"

envBackend = f"NODE_ENV={nodeEnv}\n\n"\
      f"PORT={virtualPortBack}\n"\
      f"JWT_SECRET={jwtSecret}\n"\
      f"CORS_ORIGIN={corsOrigin}\n"


# WRITE TO ENV FILES
with open('./.env.frontend', 'w+') as f:
    print('Creating ./.env.frontend')
    f.write(envContainerFront)

with open('./.env.backend', 'w+') as f:
    print('Creating ./.env.backend')
    f.write(envContainerBack)

# WRITE TO APP ENV FILES
with open('./frontend/.env', 'w+') as f:
    print('Creating ./frontend/.env')
    f.write(envFrontend)

with open('./backend/.env', 'w+') as f:
    print('Creating ./backend/.env')
    f.write(envBackend)


print("\n")
print('DONE!')
