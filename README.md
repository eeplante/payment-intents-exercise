# payment-intents-exercise

Created using the framework from https://github.com/stripe-samples/react-elements-card-payment

To run the app locally the following must be installed: 

		NPM

		Node

		Stripe

		Winston
		
		Python 3.x

1. Clone the repository (https://github.com/eeplante/payment-intents-exercise.git)


2. At the command line, navigate to the server directory (cd server)

		NPM Start

		This will start the server at http://localhost:4242/

3. At the command line, navigate to the client directory (cd client)

		NPM Start

		This will launch the app at http://localhost:3000/

4. At the command line, navigate to the root folder of the project
		
		Python cherryserver.py

		This will launch the cherry server at http://localhost:8080/
		

Logging:

Every successful payment logs to 'combined.log' using winston 3.3.3

Every payment attempt writes to cherry server and to data_file.json
