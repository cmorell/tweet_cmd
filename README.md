# Twitter CMD

A sample to publish a tweet in user timeline.

## Requeriments and installation
Python (2.7.3v)

Install (if you don't have it) Python:
```bash
sudo apt-get install python2.6
```

Install tweepy module using install.sh script
```bash
./install.sh
```

##Configure Python script
1. Go to [App developer twitter page](https://apps.twitter.com/) and sign up with a twitter account.
2. Create a new App
3. Go to Permissions Page of createad App and change to Read and Write
4. Go to Keys and Access Tokens and regenerate Consumer Key and Secret and also My Access Token and Token Secret
5. Full config.py file with the return values

```bash
cat config.py.sample > config.py
```
