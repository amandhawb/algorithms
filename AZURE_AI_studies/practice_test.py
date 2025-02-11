# Which natural language processing (NLP) technique normalizes words before counting them?
# Select only one answer.
# a) frequency analysis
# b) N-grams
# c) stemming --> Correct.
# d) vectorization
# --> Stemming normalizes words before counting them. Frequency analysis counts how often a word appears in a text. N-grams extend frequency analysis to include multi-term phrases. Vectorization captures semantic relationships between words by assigning them to locations in n-dimensional space.

# What is the first step in the statistical analysis of terms in a text in the context of natural language processing (NLP)?
# Select only one answer.
# creating a vectorized model
# counting the occurrences of each word
# encoding words as numeric features
# removing stop words --> Correct
# --> Removing stop words is the first step in the statistical analysis of terms used in a text in the context of NLP. Counting the occurrences of each word takes place after stop words are removed. Creating a vectorized model is not part of statistical analysis. It is used to capture the sematic relationship between words. Encoding words as numeric features is not part of statistical analysis. It is frequently used in sentiment analysis.

# What is the confidence score returned by the Azure AI Language detection service of natural language processing (NLP) for an unknown language name?
# Select only one answer.
# 1
# -1
# NaN --> Correct
# Unknown
# --> NaN, or not a number, designates an unknown confidence score. Unknown is a value with which the NaN confidence score is associated. The score values range between 0 and 1, with 0 designating the lowest confidence score and 1 designating the highest confidence score.

# Which part of speech synthesis in natural language processing (NLP) involves breaking text into individual words such that each word can be assigned phonetic sounds?
# Select only one answer.
# lemmatization
# key phrase extraction
# tokenization --> Correct
# transcribing
# --> Tokenization is part of speech synthesis that involves breaking text into individual words such that each word can be assigned phonetic sounds. Transcribing is part of speech recognition, which involves converting speech into a text representation. Key phrase extraction is part of language processing, not speech synthesis. Lemmatization, also known as stemming, is part of language processing, not speech synthesis.

# For which two scenarios is the Universal Language Model used by the speech-to-text API optimized? Each correct answer presents a complete solution.
# Select all answers that apply.
# acoustic
# conversational --> Correct
# dictation --> Correct
# language
# pronunciation
# --> The Universal Language Model used by the speech-to-text API is optimized for conversational and dictation scenarios. The acoustic, language, and pronunciation scenarios require developing your own model.

# Which type of translation does the Azure AI Translator service support?
# Select only one answer.
# speech-to-speech
# speech-to-text
# text-to-speech
# text-to-text --> Correct
# --> The Azure AI Translator service supports text-to-text translation, but it does not support speech-to-text, text-to-speech, or speech-to-speech translation.

# Which Azure resource provides direct access to both Azure AI Translator and Azure AI Speech services through a single endpoint and authentication key?
# Select only one answer.
# Azure AI Bot Service
# Azure AI Services --> Correct
# Azure Machine Learning
# Azure AI Language service
# --> Azure AI Services provides direct access to both Azure AI Translator and Azure AI Speech services through a single endpoint and authentication key. Azure AI Language service can be used to access the Azure AI Language service, but not the Azure AI Translator and Azure AI Speech services. The Machine Learning service is used to design, implement, and deploy Machine Learning models. Azure AI Bot Service provides a framework for developing, publishing, and managing bots in Azure.

# Which three features are elements of the Azure AI Language Service? Each correct answer presents a complete solution.
# Select all answers that apply.
# Azure AI Vision
# Azure AI Content Moderator
# Entity Linking --> Correct
# Personally Identifiable Information (PII) detection --> Correct
# Sentiment analysis --> Correct
# Entity Linking, PII detection, and sentiment analysis are all elements of the Azure AI Service for Azure AI Language. Azure AI Vision deals with image processing. Azure AI Content Moderator is an Azure AI Services service that is used to check text, image, and video content for material that is potentially offensive.

# When using the Azure AI Service for Language, what should you use to provide further information online about entities extracted from a text?
# Select only one answer.
# entity linking --> Correct
# key phrase extraction
# named entity recognition
# text translation
# --> Entity Linking identifies and disambiguates the identity of entities found in a text. Key phrase extraction is not used to extract entities and is used instead to extract key phrases to identify the main concepts in a text. Named entity recognition cannot provide a link for each entity to view further information. Text translation is part of the Azure AI Translator service.

# Which artificial intelligence (AI) technique should be used to extract the name of a store from a photograph displaying the store front?
# Select only one answer.
# image classification
# natural language processing (NLP)
# optical character recognition (OCR) --> Correct
# semantic segmentation
# --> OCR provides the ability to detect and read text in images. NLP is an area of AI that deals with identifying the meaning of a written or spoken language, but not detecting or reading text in images. Image classification classifies images based on their contents. Semantic segmentation provides the ability to classify individual pixels in an image.

# Which two specialized domain models are supported by Azure AI Vision when categorizing an image? Each correct answer presents a complete solution.
# Select all answers that apply.
# celebrities --> Correct
# image types
# landmarks --> Correct
# people_
# people_group
# --> When categorizing an image, the Azure AI Vision service supports two specialized domain models: celebrities and landmarks. Image types is an additional capability of the computer vision service, allowing it to detect the type of image, such as a clip art image or a line drawing. Both people_ and people_group are supported categories when performing image classification.

# Which process allows you to use object detection?
# Select only one answer.
# analyzing sentiment around news articles
# extracting text from manuscripts
# granting employee access to a secure building
# tracking livestock in a field --> Correct
# --> Object detection can be used to track livestock animals, such as cows, to support their safety and welfare. For example, a farmer can track whether a particular animal has not been mobile. Sentiment analysis is used to return a numeric value based on the analysis of a text. Employee access to a secure building can be achieved by using facial recognition. Extracting text from manuscripts is an example of a computer vision solution that uses optical character recognition (OCR).

# You have a set of images. Each image shows one type of bone fracture. What allows you to identify bone fractures in different X-ray images?
# Select only one answer.
# conversational artificial intelligence (AI)
# facial detection
# image classification --> Correct
# object detection
# --> Image classification is part of computer vision and can be used to evaluate images from an X-ray machine to quickly classify specific bone fracture types. This helps improve diagnosis and treatment plans. An image classification model is trained to facilitate the categorizing of the bone fractures. Object detection is used to return identified objects in an image, such as a cat, person, or chair. Conversational AI is used to create intelligent bots that can interact with people by using natural language. Facial detection is used to detect the location of human faces in an image.

# You have a set of images. Each image shows multiple vehicles. What allows you to identity different vehicle types in the same traffic monitoring image?
# Select only one answer.
# image classification
# linear regression
# object detection --> Correct
# optical character recognition (OCR)
# --> Object detection can be used to evaluate traffic monitoring images to quickly classify specific vehicle types, such as car, bus, or cyclist. Linear regression is a machine learning training algorithm for training regression models. Image classification is part of computer vision that is concerned with the primary contents of an image. OCR is used to extract text and handwriting from images.

# Which analytical task of the Azure AI Vision service returns bounding box coordinates?
# Select only one answer.
# image categorization
# object detection --> Correct
# optical character recognition (OCR)
# tagging
# --> Detecting objects identifies common objects and, for each, returns bounding box coordinates. Image categorization assigns a category to an image, but it does not return bounding box coordinates. Tagging involves associating an image with metadata that summarizes the attributes of the image, but it does not return bounding box coordinates. OCR detects printed and handwritten text in images, but it does not return bounding box coordinates.

# Which additional piece of information is included with each phrase returned by an image description task of the Azure AI Vision?
# Select only one answer.
# bounding box coordinates
# confidence score --> Correct
# endpoint
# key
# --> Each phrase returned by an image description task of the Azure AI Vision includes the confidence score. An endpoint and a key must be provided to access the Azure AI Vision service. Bounding box coordinates are returned by services such as object detection, but not image description.

# Which two Azure AI Document Intelligence models include identifying common data fields as part of its data extraction capabilities? Each correct answer presents a complete solution.
# Select all answers that apply.
# business card model --> Correct
# general document model
# invoice model --> Correct
# layout model
# read model
# --> The business card model analyzes and extracts key information from business card images and includes common data field extractions, such as name and email. The invoice model extracts key information from sales invoices and includes common data fields used in invoices for extraction. The read model, layout model, and general document model do not identify and extract common data fields.

# When using the Face Detect API of the Azure AI Face service, which feature helps identify whether a human face has glasses or headwear?
# Select only one answer.
# face attributes
# face ID
# face landmarks
# face rectangle
# --> Face attributes are a set of features that can be detected by the Face Detect API. Attributes such as accessories (glasses, mask, headwear etc.) can be detected. Face rectangle, face ID, and face landmarks do not allow you to determine whether a person is wearing glasses or headwear.

# Which service can you use to train an image classification model?
# Select only one answer.
# Azure AI Vision
# Azure AI Custom Vision --> Correct
# Azure AI Face
# Azure AI Language
# --> Azure AI Custom Vision is an image recognition service that allows you to build and deploy your own image models. The Azure AI vision service, Azure AI Face service, and Azure AI Language service do not provide the capability to train your own image model.

# Which type of machine learning algorithm assigns items to a set of predefined categories?
# Select only one answer.
# classification --> Correct
# clustering
# regression
# unsupervised
# --> Classification algorithms are used to predict a predefined category to which an input value belongs. Regression algorithms are used to predict numeric values. Clustering algorithms group data points that have similar characteristics. Unsupervised learning is a category of learning algorithms that includes clustering, but not regression or classification.

# A healthcare organization has a dataset consisting of bone fracture scans that are categorized by using predefined fracture types. The organization wants to use machine learning to detect the different types of bone fractures for new scans before the scans are sent to a medical practitioner.
# Which type of machine learning is this?
# Select only one answer.
# classification  --> Correct
# clustering
# featurization
# regression
# --> Classification is used to predict categories of data. It can predict which category or class an item of data belongs to. In this example, a machine learning model trained by using classification with labeled data can be used to determine the type of bone fracture in a new scan that is not labeled already. Featurization is not a machine learning type. Regression is used to predict numeric values. Clustering analyzes unlabeled data to find similarities in the data.

# You plan to use machine learning to predict the probability of humans developing diabetes based on their age and body fat percentage.
# What should the model include?
# Select only one answer.
# three features
# three labels
# two features and one label --> Correct
# two labels and one feature
# --> The scenario represents a model that is meant to establish a relationship between two features (age and body fat percentage) and one label (the likelihood of developing diabetes). The features are descriptive attributes (serving as the input), while the label is the characteristic you are trying to predict (serving as the output).

# In a regression machine learning algorithm, what are the characteristics of features and labels in a validation dataset?
# Select only one answer.
# known feature and label values --> Correct
# known feature values and unknown label values
# unknown feature and label values
# unknown feature values and known label values
# --> In a regression machine learning algorithm, a validation set contains known feature and label values.

# A company is using machine learning to predict various aspects of its e-scooter hire service dependent on weather. This includes predicting the number of hires, the average distance traveled, and the impact on e-scooter battery levels.
# For the machine learning model, which two attributes are the features? Each correct answer presents a complete solution.
# Select all answers that apply.
# distance traveled
# e-scooter battery levels
# e-scooter hires
# weather temperature --> Correct
# weekday or weekend --> Correct
# --> Weather temperature and weekday or weekend are features that provide a weather temperature for a given day and a value based on whether the day is on a weekend or weekday. These are input variables for the model to help predict the labels for e-scooter battery levels, number of hires, and distance traveled. E-scooter battery levels, number of hires, and distance traveled are numeric labels you are attempting to predict through the machine learning model.

# A company wants to predict household water use based on the number of people in a house, the weather temperature, and the time of year.
# In terms of data labels and features, what is the label in this use case?
# Select only one answer.
# number of people in the house
# time of year
# water use --> Correct
# weather temperature
# --> Water use is the label value that you want to predict, also known as the independent variable. Number of people in the house, weather temperature, and time of year are features, and are values that are dependent on the label. Number of people in the house, weather temperature, and time of year can influence the water consumed in a household.

# What should you do after preparing a dataset and before training the machine learning model?
# Select only one answer.
# clean missing data
# normalize the data
# split data into training and validation datasets --> Correct
# summarize the data
# --> Splitting data into training and validation datasets leaves you with two datasets, the first and largest of which is the training dataset you use to train the model. The second, smaller dataset is the held back data and is called the validation dataset, as it is used to evaluate the trained model. If normalizing or summarizing the data is required, it will be carried out as part of data transformation. Cleaning missing data is part of preparing the data and the data transformation processes.

# You need to use Azure Machine Learning to train a regression model.
# What should you create in Machine Learning studio?
# Select only one answer.
# a job --> Correct
# a workspace
# an Azure container instance
# an Azure Kubernetes Service (AKS) cluster
# --> A job must be created in Machine Learning studio to use Machine Learning to train a regression model. A workspace must be created before you can access Machine Learning studio. An Azure container instance and an AKS cluster can be created as a deployment target, after training of a model is complete.

# You train a regression model by using automated machine learning (automated ML) in the Azure Machine Learning studio. You review the best model summary.
# You need to publish the model for others to use from the internet.
# What should you do next?
# Select only one answer.
# Create a compute cluster.
# Deploy the model to an endpoint. --> Correct
# Split the data into training and validation datasets.
# Test the deployed service.
# --> You can deploy the best performing model for client applications to use over the internet by using an endpoint. Compute clusters are used to train the model and are created directly after you create a Machine Learning workspace. Before you can test the model’s endpoint, you must deploy it first to an endpoint. Automated ML performs the validation automatically, so you do not need to split the dataset.

# Which three supervised machine learning models can you train by using automated machine learning (automated ML) in the Azure Machine Learning studio? Each correct answer presents a complete solution.
# Select all answers that apply.
# Classification --> Correct
# Clustering
# inference pipeline
# regression --> Correct
# time-series forecasting --> Correct
# --> Time-series forecasting, regression, and classification are supervised machine learning models. Automated ML learning can predict categories or classes by using a classification algorithm, as well as numeric values as part of the regression algorithm, and at a future point in time by using time-series data. Inference pipeline is not a machine learning model. Clustering is unsupervised machine learning and automated ML only works with supervised learning algorithms.

# Which three data transformation modules are in the Azure Machine Learning designer? Each correct answer presents a complete solution.
# Select all answers that apply.
# Clean Missing Data --> Correct
# Model Evaluate Model
# Normalize Data --> Correct
# Select Columns in Dataset --> Correct
# Train Clustering
# --> Normalize Data is a data transformation module that is used to change the values of numeric columns in a dataset to a common scale, without distorting differences in the range of values. The Clean Missing Data module is part of preparing the data and data transformation process. Select Columns in Dataset is a data transformation component that is used to choose a subset of columns of interest from a dataset. The train clustering model is not a part of data transformation. The evaluate model is a component used to measure the accuracy of training models.

# What is an unsupervised machine learning algorithm module for training models in the Azure Machine Learning designer?
# Select only one answer.
# Classification
# K-Means Clustering --> Correct
# Linear Regression
# Normalize Data
# --> K-means clustering is an unsupervised machine learning algorithm component used for training clustering models. You can use unlabeled data with this algorithm. Linear regression and classification are supervised machine learning algorithm components. You need labeled data to use these algorithms. Normalize Data is not a machine learning algorithm module.

# Which three sources can be used to generate questions and answers for a knowledge base? Each correct answer presents a complete solution.
# Select all answers that apply.
# a webpage --> Correct
# an audio file
# an existing FAQ document --> Correct
# an image file
# manually entered data --> Correct
# --> A webpage or an existing document, such as a text file containing question and answer pairs, can be used to generate a knowledge base. You can also manually enter the knowledge base question-and-answer pairs. You cannot directly use an image or an audio file to import a knowledge base.

# Select the answer that correctly completes the sentence.
# [Answer choice] use plugins to provide end users with the ability to get help with common tasks from a generative AI model.
# Select only one answer.
# Copilots --> Correct
# Language Understanding solutions
# Question answering models
# RESTful API services
# --> Copilots are often integrated into applications to provide a way for users to get help with common tasks from a generative AI model. Copilots are based on a common architecture, so developers can build custom copilots for various business-specific applications and services.

# At which layer can you apply content filters to suppress prompts and responses for a responsible generative AI solution?
# Select only one answer.
# metaprompt and grounding
# model
# safety system --> Correct
# user experience
# --> The safety system layer includes platform-level configurations and capabilities that help mitigate harm. For example, the Azure OpenAI service includes support for content filters that apply criteria to suppress prompts and responses based on the classification of content into four severity levels (safe, low, medium, and high) for four categories of potential harm (hate, sexual, violence, and self-harm).

# Select the answer that correctly completes the sentence.
# [Answer choice] can return responses, such as natural language, images, or code, based on natural language input.
# Select only one answer.
# Computer vision
# Deep learning
# Generative AI --> Correct
# Machine learning
# Reinforcement learning
# --> Generative AI models offer the capability of generating images based on a prompt by using DALL-E models, such as generating images from natural language. The other AI capabilities are used in different contexts to achieve other goals.

# Select the answer that correctly completes the sentence.
# [Answer choice] can used to identify constraints and styles for the responses of a generative AI model.
# Select only one answer.
# Data grounding
# Embeddings
# System messages --> Correct
# Tokenization
# --> System messages should be used to set the context for the model by describing expectations. Based on system messages, the model knows how to respond to prompts. The other techniques are also used in generative AI models, but for other use cases.

# Which two capabilities are examples of a GPT model? Each correct answer presents a complete solution.
# Select all answers that apply.
# Create natural language. --> Correct
# Detect specific dialects of a language.
# Generate closed captions in real-time from a video.
# Synthesize speech.
# Understand natural language. --> Correct
# --> Azure OpenAI natural language models can take in natural language and generate responses. GPT models are excellent at both understanding and creating natural language.

# You plan to develop an image processing solution that will use DALL-E as a generative AI model.
# Which capability is NOT supported by the DALL-E model?
# Select only one answer.
# image description --> Correct
# image editing
# image generation
# image variations
# --> Image description is not a capability included in the DALL-E model, therefore, it is not a use case that can be implemented by using DALL-E, while the other three capabilities are offered by DALL-E in Azure OpenAI.

# Which generative AI model is used to generate images based on natural language prompts?
# Select only one answer.
# DALL-E --> Correct
# Embeddings
# GPT-3.5
# GPT-4
# Whisper
# --> DALL-E is a model that can generate images from natural language. GPT-4 and GPT-3.5 can understand and generate natural language and code but not images. Embeddings can convert text into numerical vector form to facilitate text similarity. Whisper can transcribe and translate speech to text.

# Select the answer that correctly completes the sentence.
# [Answer choice] can search, classify, and compare sources of text for similarity.
# Select only one answer.
# Data grounding
# Embeddings --> Correct
# Machine learning
# System messages
# --> Embeddings is an Azure OpenAI model that converts text into numerical vectors for analysis. Embeddings can be used to search, classify, and compare sources of text for similarity.

# Which type of service provides a platform for conversational artificial intelligence (AI)?
# Select only one answer.
# Azure AI Bot Service --> Correct
# Azure AI Document Intelligence
# Azure AI Vision
# Azure AI Translator
# --> Azure AI Bot Service provide a platform for conversational artificial intelligence (AI), which designates the ability of software agents to participate in a conversation. Azure AI Translator is part of Natural language processing (NLP), but it does not serve as a platform for conversational AI. Azure AI Vision deals with image processing. Azure AI Document Intelligence extracts information from scanned forms and invoices.

# Which AI service can be integrated into chat applications and generate content in the form of text?
# Select only one answer.
# Azure AI Language
# Azure AI Metrics Advisor
# Azure AI Vision
# Azure OpenAI --> Correct
# --> Azure OpenAI is the only service capable of generating text that can be used in chat applications to create conversational experiences. The other workloads are Azure Cognitive Services used for different purposes, but not for generating text used in chat applications.

# Which type of artificial intelligence (AI) workload has the primary purpose of making large amounts of data searchable?
# Select only one answer.
# image analysis
# knowledge mining --> Correct
# object detection
# semantic segmentation
# --> Knowledge mining is an artificial intelligence (AI) workload that has the purpose of making large amounts of data searchable. While other workloads leverage indexing for faster access to large amounts of data, this is not their primary purpose.

# You are exploring solutions to improve the document search and indexing service for employees.
# You need an artificial intelligence (AI) search solution that will include searching text in various types of documents, such as images.
# Which type of AI workload is this?
# Select only one answer.
# semantic segmentation
# computer vision
# conversational AI
# data mining --> Correct
# --> Data mining workloads primarily focus on the searching and indexing of data. The computer vision can be used to extract information from images, but it is not a search and indexing solution. Conversational AI is part of natural language processing (NLP) and facilitates the creation of chatbots. Semantic segmentation provides the ability to classify individual pixels in an image depending on the object that they represent.

# Which two artificial intelligence (AI) workload features are part of the Azure AI Vision service? Each correct answer presents a complete solution.
# Select all answers that apply.
# entity recognition
# key phrase extraction
# optical character recognition (OCR) --> Correct
# sentiment analysis
# spatial analysis --> Correct
# --> OCR and Spatial Analysis are part of the Azure AI Vision service. Sentiment analysis, entity recognition, and key phrase extraction are not part of the computer vision service.

# Which principle of responsible artificial intelligence (AI) raises awareness about the limitations of AI-based solutions?
# Select only one answer.
# accountability
# privacy and security
# reliability and safety
# transparency --> Correct
# --> Transparency provides clarity regarding the purpose of AI solutions, the way they work, as well as their limitations. The privacy and security, reliability and safety, and accountability principles focus on the capabilities of AI, rather than raising awareness about its limitations.

# Which principle of responsible artificial intelligence (AI) has the objective of ensuring that AI solutions benefit all parts of society regardless of gender or ethnicity?
# Select only one answer.
# accountability
# inclusiveness --> Correct
# privacy and security
# reliability and safety
# --> The inclusiveness principle is meant to ensure that AI solutions empower and engage everyone, regardless of criteria such as physical ability, gender, sexual orientation, or ethnicity. Privacy and security, reliability and safety, and accountability do not discriminate based on these criteria, but also do not emphasize the significance of bringing benefits to all parts of the society.

# Which principle of responsible artificial intelligence (AI) defines the framework of governance and organization principles that meet ethical and legal standards of AI solutions?
# Select only one answer.
# accountability --> Correct
# fairness
# inclusiveness
# transparency
# --> Accountability defines the framework of governance and organizational principles, which are meant to ensure that AI solutions meet ethical and legal standards that are clearly defined. The other answer choices do not define the framework of governance and organization principles, but provide guidance regarding the ethical and legal aspects of the corresponding standards.

# Which principle of responsible artificial intelligence (AI) plays the primary role when implementing an AI solution that meet qualifications for business loan approvals?
# Select only one answer.
# accountability
# fairness --> Correct
# inclusiveness
# safety
# --> Fairness is meant to ensure that AI models do not unintentionally incorporate a bias based on criteria such as gender or ethnicity. Transparency does not apply in this case since banks commonly use their proprietary models when processing loan approvals. Inclusiveness is also out of scope since not everyone is qualified for a loan. Safety is not a primary consideration since there is no direct threat to human life or health in this case.

# Which two principles of responsible artificial intelligence (AI) are most important when designing an AI system to manage healthcare data? Each correct answer presents part of the solution.
# Select all answers that apply.
# accountability --> Correct
# fairness
# inclusiveness
# privacy and security --> Correct
# --> The accountability principle states that AI systems are designed to meet any ethical and legal standards that are applicable. The system must be designed to ensure that privacy of the healthcare data is of the highest importance, including anonymizing data where applicable. The fairness principle is applied to AI systems to ensure that users of the systems are treated fairly. The inclusiveness principle states that AI systems must empower people in a positive and engaging way.