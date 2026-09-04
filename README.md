# Artificial Intelligence for Developers in Easy Steps

Artificial Intelligence for Developers in Easy Steps, Richard Urwin © 2024 by In Easy Steps Limited.

**ELIZA**  
- Ch.2 - Simple chatbot based on the 1966 ELIZA program by Joseph Weizenbaum.

**Dolittle**  
- Ch.3 - A simple expert system, animal guessing game. Currently allows player to add to knowledge base.

**Flatworld**  

<ul>
	<li>
- Ch.4 - A pygame is setup with predators (red ball) chasing a user controlled player (blue ball) on a game board, with random grass (green spikes) for the player to eat.
	</li>
	<li>
- Ch.5 - Replaced user controlled player with fuzzy logic bots (blue ball) that either feed on the grass or run away from the predators depending on how scared they are (proximity to red ball).
	</li>
	<li>
- Ch.6 - Improved fuzzy bots (blue ball) with subsumption with dinstinct wander/feed/flee behaviors. By adding the subsumption, the fuzzy bots survive much longer and do not get stuck on the walls or corners of the game board.
	</li>
	<li>
- Ch.7 - Using the previous Flatworld board, we now have bees finding flowers. Genetic algorithms are used to mutate the bees' chromosomes after each generation to better improve their efficiency. Machine Learning.
	</li>
	<li>
- Ch.8 - Returning the predators and grass eating herbivores to the Flatworld, we include genetics from the previous chapter and implement a neural network for the movement of each type of creature. TensorFlow and NumPy used.
	</li>
</ul>

**Pretrained Neural Netwrok**  
<ul>
	<li>
- Ch.9 - Setting up and pretraining a model for recognizing hand-written digits, then testing it on your own written numbers.
	</li>
	<li>
- Prepare and Process user created input images of hand-written digits. Write down a series of numbers, the SplitChar program will locate each digit and separate them into negative output images. Note: overlapping numbers will be captured as 1 number and random marks will show up and be included in the data, so a double-check is currently needed. TensorFlow and MatplotLib.
	</li>
	<li>
- Runs the user created images output folder through a new model instance of the pretrained model from earlier and prints what the model predicted was the user created hand-written numbers.
	</li>
</ul>

**Generative AI**  
<ul>
	<li>
- Ch.10 - Generating a list of baby names, trained on the National Records of Scotland statistics for Babies' First Names. This program reads in a csv file with baby names registered in Scotland from 1974 to 2023, collects all the characters used, batches combinations to analyze, and generates a list of possible new and unique baby names. (note: suggests running this with GPU. mine took ~7 minutes per epoch w/o GPU)
	</li>
</ul>

**Low Code**
<ul>
	<li>
- Ch. 11 - Setting up Docker Desktop, using a pycaret image, we use a jupyter notebook to evaluate and optimize a dataset provided by PyCaret about forecasting the onset of diabetes.

