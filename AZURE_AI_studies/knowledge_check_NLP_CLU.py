# 1. You need to provision an Azure resource that will be used to author a new conversational language understanding application. What kind of resource should you create? 
# Azure AI Speech
# Azure AI Language --> Correct
# Azure AI services

# 2. You are authoring a conversational language understanding application to support an international clock. You want users to be able to ask for the current time in a specified city, for example "What is the time in London?". What should you do? 
# Define a "city" entity and a "GetTime" intent with utterances that indicate the city entity. --> Correct
# Create an intent for each city, each with an utterance that asks for the time in that city.
# Add the utterance "What time is it in city" to the "None" intent.

# 3. You have published your conversational language understanding application. What information does a client application developer need to get predictions from it? 
# The endpoint and key for the application's prediction resource --> Correct
# The endpoint and key for the application's authoring resource
# The Azure credentials of the user who published the language understanding application