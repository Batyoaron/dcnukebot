# discord nuke bot

How to invite the bot to the server

Go to the Discord Developer Portal and log in with your Discord account.

Once logged in, click on the "New Application" button.

Give your application a name (this will be the name of your bot).

After creating the application, click on the "Bot" tab on the left sidebar, then click on the "Add Bot" button to create a bot user for your application.

You'll see a "Token" section where you can copy your bot's token. Make sure to keep this token secure and never share it publicly. (And paste that token into the python program(TOKEN = "YOUR BOT ID"))

Next, go to the "OAuth2" tab on the left sidebar. Scroll down to the "OAuth2 URL Generator" section.

Under "Scopes", select "bot".

Under "Bot Permissions", select the permissions your bot will need. For the bot we created earlier (the one that deletes channels), it will need the "Manage Channels" permission.

After selecting the appropriate permissions, a URL will be generated. With that url you can invite the bot to the server.
