## Touchscreen Interaction
- touch is thought to be the first sense humans develop
- sense of touch, tactile sense is made up of exceptionally fine network of receptors in ytour skin
- **Sensors for Finger Input Detection**-
	- two main types of screen sensors for finder input detection
		- **Resistive Touchscreen**-
			- works based on pressure applied to the screen
			- consists of several layers
			- when screen is pressed, the outer layer is pushed onto the next layer
			- the technology senses the pressure is being applied and registers input
			- while versatile as they can be used with finger, fingernail, stylus or any other object
			- they are used on pen-based interfaces
		- **Capacitive Touchscreens**-
			- work by sensing the conductive properties of an object usually the skin on your fingertip
			- screen on a mobile phone or smartphone usually has a glass face and does not rely on pressure
			- makes it more responsive than resistive screen when it comes to gestures such as swiping and pinching
			- can only be touched with a finger (some conductive pens)
			- will not respond to touches with a regular stylus, gloves or most other objects
	- actions like swiping through contact lists, zooming in and out of web pages and maps, scrolling though photos are best suited to capacitive touchscreens, unlike resistive screens you can swipe across them gently and still get a response
- **Touchscreens vs Touchpads**-
	- compare through 3 aspects- 
		- **Precision**-
			- **Touchscreens**-
				- Low
				- the contact area of fingertup is greater than a single x, y coordinate, which increases the chances of uninteded command activiations
				- mouse and pen/stylus supply a precise x, y coordinate
			- **Touchpads**-
				- High
				- same as a mouse
		- **Object State**-
			- **Touchscreens**-
				- two state model
				- touch surface of a display device is either touched (on) or not (off)
				- no hover state that ca n trigger additional visual feedback
			- **Touchpads**-
				- same as touch
		- **Rich Interaction**-
			- **Touchscreens**-
				- supports multitouch
				- multiple input points (fingertips) on a touch surface
				- supports direct manipulation of objects through gestures such as tapping, dragging, sliding, pinching and rotating
			- **Touchpads**-
				- same as touch
				- no support for direct manipulation as they are indirect input devices
- **Two-State Model**-
	- direct finger touch uses a two-state model
		- touch surface of a display device is either touched (on) or not (off)
		- there is no hover state that can trigger addiitional visual feedback
		- ![[Pasted image 20250805094126.png]]
- **Multitouch**-
	- multitouch tech that enables a touchpad or touchscreen to recognise more than one point of contact with the surface
	- apple added in multi-touch with additional functionality such as pinch, zoom or to activate certain subroutines to predefined gestures
	- increases the degree of freedom for finger input
	- commonly a finger can just offer two degrees of freedom (x, y coordinates) which is required for pointing tasks
	- higher degrees of freedom can be achieved with more fingers engaged in interaction tasks
	- multitouch tech can be used to perform other tasks such as zooming and rotation- which is significant advantage of the multitouch technology
	- current multiotouch tech are actually multippoint because they only rely on information of x,y coordinates
- **Finger Properties**-
	- classified into 4 main categories
		- **Position Property**
			- coordinage value (x,y)
		- **Motion Property**-
			- velcoity
			- acceleration
		- **Physical Property**-
			- size of contact area
			- shape of contact area
			- orientation
			- pressure
		- **Even Property**-
			- finger tap
			- finger flick
	- The contact position of the finger is the first property considered in widget design
	- most touchscreen devices can detect and track single point on the touch panel of device
	- touch interaction design also considered finger movement velocity and acceleration
	- dictionary entries include a variety of motions and may take form of dedicated computer app
	- researchers also investigated finger physucal properties
		- when finger lands on a touchscreen there are physical properties such as finger contact area, finger orientation and finger pressure that can be used to enhance finger interaction
		- ![[Pasted image 20250806085529.png]]
	- finger tapping is typically adopted to simluate the mouse click event. finger flicking is a quick movement on the screen and used as the primary navigation gesture
- **Fat Finger Problem**-
	- when selecting targets on touch device with a finger and the targets are smaller than the size of the finger contact area users do not know if they hit the desired target
	- lack of sensing precision can make precise touchscreen interactions more difficult and error prone
	- in many interfaces touch targets are packed too close toegether resulting in wrong button being touched which ends up as incorrect input
	- **Solutions**-
		- **Pinch Gesture**-
			- enlarge the target to be selected
			- user touches screen with two or more fingers and moves them apart to zoom in
		- **Shift**-
			- facilitate target selection on touchscreen
			- Scenario 1
				1. user touches screen intending to acquire small target located near other targets; shift determines the presense of targets small enough to be occluded by the finger
				2. to eliminate occlusion, shift 'escalates' by creating a callout that contains a copy of the occluded screen area placed in a non occluded location on the screen; the callout includes a pointer representing the finger contact point to eliminate selection point abiguity
				3. the user fine-tunes the pointer position while maintaing contact with the screen
				4. once the correct position is visually verified, lifting the finger to select the target
				5. removes the callout
			- Scenario 2
				- when acquiring a large target, shift behaves differently. occlusion is not a problem in this case, so shift does not escalate by default.
				- lifting their finger immediately, user makes selection as if using an unaided touchscreen
				- ![[Pasted image 20250807151238.png]]
		- **Lucidtouch**-
			- is a mobile device that is 'pseudo transparent'
			- allows users to see their fingers through the screen
			- users interact with screen contents using multiple fingers on the back of the device
			- this solves the problem that traditional touchscreens are facing; it prevents the users fingers from occluding screen contents

## Pen Interaction
- pen interaction has attacted a lot of attention in HCI
- a stylus (digital pen) is a small, pen shaped instrument used to input commands to a computer screen, mobile device or graphics tablet
- user places a stylus on the surface of the screen to draw or make selections by tapping the stylus on the screen
- stylus can be used instead of a mouse or trackpad
- **Pen Computing**-
	- follows a pen-paper metaphor
	- fundamental way for capturing daily experiences, communicating ideas, recording notable events and conducting deep thinking and visual descriptions
- **Properties of Pen Input**-
	- two types input device
		- **Absolute Input Device**-
			- one-to-one mapping between input and output spaces
		- **Direct Input Device**-
			- display surface is also the input surface
	- **Three State Model**- graphics tablet with stylus
		- state 0 the stylus is off the tablet and tip switch is in open state
		- moving stylus has no effect since it is out of range
		- when stylus in range, tracking symbol follows the stylus motion (state 1: tracking)
		- extra pressure on the stylus closes the tip switch moving system to state 2
		- ![[Pasted image 20250807161113.png]]
	- **Two Modes Pen Interfaces**-
		- **Inking**-
			- allows data entry
			- gestures are drawn to issue commands for manipulating the data
			- example- note-taking tool allows people to take notes via natural handwriting (inking) and to edit by making copy editing gestured to perform commands (gesturing)
			- can support scratching out a word in some sytems, if not in a system then it can create naturally occuring ink stroks by accident which are classified as gestures
		- **Gesturing**-
			- things like shading or something
	- **Pen Properties**-
		- five basic pen properties
			- **x,y Coordinate**: x,y movements of pen are sensed on tablet surface
			- **Pen Pressure**: amount of pressure applied by the pen tip on the tablet surface
			- **Pen Tilt**: angle between the pen barrel and projection of the pen barrel on the screen
			- **Pen Rolling**: movements by turning over and over along the pen barrel (lon axis)
			- **Pen Azimuth**: angle between north direction and projection of the pen barrel on the screen
		- ![[Pasted image 20250807161615.png]]
		- **Interacting with Large Screens**-
			- when working at large wall display, even if partially utilised, many targets are likely to be distant from the user, requiring walking, which is slow and inerrupts workflor- need to design techniques for remote target selection
		- **Gesture Select Technique**-
			1. user identifies a remote target they wish to select
			2. a continuation marks appear on the targets
				1. user draws an initial mark with the pen in the general diretion of the target
				2. user continues the initial mark by drawing the continuation mark of the desired target
			3. the target is selected on pen up
		- **The Vacuum Technique**-
			- interaction technique that enables quick access to items on areas of a large display that are difficult for a user to reach without significant physical movement
			- circular widget with a user-controllable arc of influence that is centered at the widgets point of invocation and spans out to the edges of the display
			- farawar objects residing inside this influence arc are brought closer to the widgets centre in the form of proxies that can be manipulated in lieue of the original
			- steps of tehcnique
				1. cursor drag beings in centre of displau
				2. when drag exceeds threshold, vacuum is invoked 20 degrees initial arc, bringing proxies of targets 3, 5 towards the centre
				3. additional cursor movement increases arc angle
				4. change in cursor direction changes direction of arc
				5. cursor moving beyond the arcs edges expands the arc
				6. cursor moving beyond the arcs edges expands the arc

## Gesture Interaction
- form of non-verbal communication which visible bodily actions are used to communicate important messages either in place of speech or together and in parallel with spoken words
- gestures include movement of the hands, face or other parts of the body'
- human gestures are a mode of non-verbal interaction and can provide most intuitive and natural way to interact with computers therefore gestures have been made in many interface designs- flick finger on screen to navigate a document
- stroke gestures are a form of 2-dimensional geometric signals from the users mind to the computer that encode texts or commands
- they are transmitted through a channel with noise (due to inaccuracies in recall and production), received by the computer and decoded by a recogniser into the messages intended by the user
- decoding process may take place at the end of the stroke or incrementally during the production of the stroke
- capacity of this channel depends on how many messages can be accurately transmitted
- this is turn depends on both users ability and computers algorithm to accurately classify different stroke gestures
- ![[Pasted image 20250807164757.png]]
- **Gesture Categories**-
	- **Touch Gestures vs Motion Gestures**-
		- touch gestures are gestures drawn on 2D screens and motion gestures are performed in the air
		- touch gestures include one-stroke gestures and multi-stroke gestures
	- **Analogue Gestures vs Abstract Gestures** -
		- analogue gestures are those that mimic physisal or conventional effects of the real world
		- analogue gesture is analogous to what a stroke gesture would do in the physical world or according to cultural convention (example- flick/swip gestures)
		- abstract gestures are fundamentally arbitraty gestures that do not resemble physucal effects (example drawing X to close a window)
	- **Application Examples of Gesture INteraction**-
		- gestures can be used to triugger commands
		- frequently used single touch gestures include:
			- tap and double tap which correspond to a single or double click
			- drag, where an objet is moved with a  continous finger movement
			- zoom, when pinching two or more finger together or apart
			- flick, where moving a finger extremely fast (to enable scrolling or to switch between windows)
		- **Google Gesture Search**-
			- enables users to search their phones contacts, bookmarks, applications and music by scribbling out letters with their fingers
		- **Gesture Keyboards**-
			- enable users to write each word in lexicon via a word gesture
			- word gesture approx traces all letters in the internded word, regardless of whether they are adjacent
			- example- write the word 'method' a user touches the 'm' key and slides to 'e' and then slides to the rest
	- **Advantages of Gesture Interaction**-
		- gesture based interfaces have two main advantages and provide the user with a completely new form of interaction
		- **Immediate and Powerful Interaction**-
			- unlike traditional buttons and menus, gestures do not interrupt the users activity by forcing them to move their hand to the location of a command
			- instead they can be performend directly from the current cursor position
		- **Intuitiveness**-
			- gestures feel very natural to perform since they mirror our experiences in the real world
			- gestures allow the user to handle multiple points of input and even define several parameters at once
			- they are a more natural form of communication
	- **Disadvantages of Gesture Interaction**-
		- gesture interaction also raises issues that are not relavant with tranditional input
		- the problems are to learn, to remember and to accurately execute gestures
		- developer must provide a syustem that correctly recognises these gestures
		- developer has to ensure gestures are qiuckly and correcctly recognised but also must provide a guide that allows a rapid and easy learning of these gestures
		- **Discoverability**-
			- they are not self-revealing or self-explanatory
			- gestures are arbitrary and are usually difficult to discover
		- **Memorability**-
			- while conventonal commands only must be recognised, gestures need to be known and remembered before executing them
			- can make them as intuitive as possible to be memorable
			- developers can design based on what they think works, but it might not be refelctive of real world human behaviour, therfore the gesture may not be intuitive
- **Gesture Recognition Algorithm $1**-
	- 2D single stroke recogniser designed for rapid prototyping of gesture based user interfaces
	- machine learning
	- recognise users drawn gesture by comparing it to a set of predefined templates in a simple way
	1. **Resample the points**
	2. **Rotate to a reference angle**
	3. **Scale to a reference square**
	4. **Translate to origin**
	5. **Compare with templates**
	6. **Pick the closest match**