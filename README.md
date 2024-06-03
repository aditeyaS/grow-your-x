<br/>

<p align="center">
  <img src="https://github.com/aditeyaS/grow-your-x/blob/main/img/logo.png" width="35%" />
  <h1 align="center">grow-your-x</h1>
  <h4 align="center">A bot that automatically tweets (posts) on Twitter (X).</h4>
  <h4 align="center">I tweet about Technology, Programming/Coding, Anime, Nature and Travel.</h4>
   <p align="center">
    <a href="https://github.com/aditeyaS/grow-your-x/actions">Check status</a>
    ·
    <a href="https://github.com/aditeyaS/grow-your-x/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/aditeyaS/grow-your-x/issues/new">Request Feature</a>
  </p>
  <div>
    <h4 align="center">Tech Stack</h4>
    <p align="center">
      <a href="https://aditeya.me">
        <img src="https://skillicons.dev/icons?i=py,flask,postman,bots,figma,twitter,vscode,github" />
      </a>
    </p>
  </div>
</p>

### How to make your own?

##### Testing the app

- Fork and clone the repo (Optional: Leave a ⭐)
- Create a .env file at the root and paste the following

```
SECRET=<a_secure_secret_message>
OPENAI_API_KEY=<openai_api_key>
OPENAI_ORGANIZATION_ID=<openai_organization_id>
OPENAI_PROJECT_ID=<openai_project_id>
X_API_KEY=<twitter_api_key>
X_API_KEY_SECRET=<twitter_api_key_secret>
X_ACCESS_TOKEN=<twitter_access_token>
X_ACCESS_TOKEN_SECRET=<twitter_access_token_secret>
```

- Replace the key values with your key. Read about getting [OpenAi key](https://platform.openai.com/docs/overview) and [Twitter key](https://developer.x.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
- Create a virtual env (Optional)

```bash
python -m venv venv
source .venv/bin/activate
```

- Install the requirements

```bash
pip install -r requirements.txt
```

- Run your app

```bash
python main.py
```

- Test you app

```
curl  -H 'Content-Type: application/json'
      -d '{"secret" : "<the_secret_you_used_above>"}' \
      -X POST \
      <your_endpoint>/api/tweet
```

- If you get a success message, congratulations! 🎉
- If you face any errors connect with me.

##### Personalizing your bot

You can personalize your bot by exploring [src/clients/OpenAI.py](https://github.com/aditeyaS/grow-your-x/blob/main/src/clients/OpenAI.py) and [src/service/generate_topic.py](https://github.com/aditeyaS/grow-your-x/blob/main/src/service/generate_topic.py)

##### Deploying your app

- Sign in/Sign up at [render.com](https://render.com/) (Recomended: use github to sign in/sign up)
- Create New web service and connect this repo
- In the **Start command** enter the following

```
gunicorn main:bot
```

- Add all the environemt variables
- Most likey your app will be deployed without errors

##### Setting up CRON job

- Go to your repository settings
- In the left sidebar, click on Secrets and variables > Actions
- Click the New repository secret button.
  - In the Name enter - URL
  - In the Secrte enter your POST endpoint which will look something like below

```
https://<your_unique_app_name>.onrender.com/api/tweet
```

- Again click the New repository secret button.
  - In the Name enter - SECRET
  - In the Secret enter - <the_secret_you_used_above>
- Go to the **cron-job.yml** file inside .github/workflows
- Under schedule update [cron](http://www.cronmaker.com/) according to your needs. (GitHub cron jobs run at UTC time)
- Push your code.

(FYI: You can also set this job through iPhone shortcut automation and many other ways)

### You are done. Happy Coding. 🎉

You can check your logs on render if you face issues.
