Setting up Google Cloud, enable Gmail API, configure OAuth consent, and create OAuth credentials for your app.
This steps are neccessary in order to run the following program successfully.

---

1. Create a Google Cloud project  
2. Enable the Gmail API  
3. Configure OAuth consent screen  
4. Create OAuth client credentials  
5. Download `client_secret.json`  
6. Add test users if you dont want to publish it

---

## 1. Create a Google Cloud Project
1. Go to Google Cloud Console.
2. Make a new project

---

## 2. Enable the Gmail API
1. In Console, open **APIs & Services → Library**.  
2. Search **Gmail API → Enable**.  

---

## 3. Configure OAuth Consent Screen
1. Go to **APIs & Services → OAuth consent screen**.  
2. Choose **Internal** (for testing) or **External** (for publishing).

---

## 4. Create OAuth Client Credentials
1. Go to **APIs & Services → Credentials → Create Credentials → OAuth client ID**. 
2. Name it, click **Create**, then **Download JSON** (`client_secret.json`).  

---

## 5. Final Steps
- Use the Client ID and Secret in your OAuth library to request Gmail access.  
- Add only the scopes you need.  

---

After this all steps are done put your client_secret.json in project's root directory and then when running first time it will make you LogIn and after a successful login it will make a gmail_token.json in which your token will be stored.

From now on whenever you run, this will use that account's gmail and read from them.

You also need a slack webhook url + a gemini api key which you can get easily.
Put that both into .env with correct env variable names.

The setup is now finished and now when you run this, it fetches your new mails summarises them and forwards that to your selected slack channel.

This all operations are automatic, and you can tweak how your mails get summarised and what response should be forwarded to your slack.