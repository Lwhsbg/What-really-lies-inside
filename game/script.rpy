transform bg_fit:
    xysize(1920,1080)
label start:
    scene black
    "{i}Your high school friends invited you to a reunion after 8 years.{/i}"
    "{i}It was in an entirely different city that you lived in, just that the cities were seperated by a dark forest.{/i}"
    "{i}Excited that you will get to see your old friends after such a long time, and find an escape for work even though it is just for a while, you immediately say yes.{/i}"
    "{i}It was only a while later when you considered that it may get a bit late in the night and will have troubles coming back.{/i}"
    "{i}But your excitement and anticipation overshadows it, even though it means driving back late at night through that creepy forest.{/i}"
    "{i}Then the day came eventually.{/i}"
    "{i}You drove and met up with them, and then you had lots of fun over the evening with them."
    "{i}But the evening went by too fast as night had fallen without you even realizing it.{/i}"
    "{i}You started to rush to your car to head back, it was nearly midnight already.{/i}"
    "{i}You got in the car to hurry back home in the dark.{/i}"
    "{i}The road was two hours long and all you could think of was how you would lay down in your bed after you reach.{/i}"
    "{i}You start driving through the city, and then eventually reach the exit gate, where infront laid the dark forest.{/i}"
    "{i}You were never really a believer of paranormal stuff, thought it was a hoax so driving at night was not really anything for you.{/i}"
    "{i}Just the issue was that you were a bit drunk and very sleepy.{/i}"
    "{i}You were aware of that, and knew you had to make this as soon as possible.{/i}"
    "{i}The sky was not so nice on you either, it was going a bit darker and darker by the moment, but you had not noticed this.{/i}"
    "{i}You go ahead into the forest.{/i}"
    "{i}It was peaceful at first. No sound, quiet driving, no cars around, straight roads.{/i}"
    "{i}Then there came the turnings part. You just went on quietly.{i}"
    "{i}Quietly.{/i}"
    "{i}Then you start feeling a bit off.{i}"
    m "{i}This feels a bit off. Like it is... Way too quiet?{/i}"
    m "{i}Maybe I should play some music.{/i}"
    "{i}Just as you approach the radio, you suddenly lose control of your steering.{/i}"
    m "FFUCC-"
    "{i}You crash into a nearby big tree in the forest.{/i}"
    m "How did that happen? I just changed my tires some days ago."
    "{i}You check on your car to find out that it is of no good to go anymore.{/i}"
    "{i}Once you realized that, you thought things could not go more wrong until the upset sky started pouring.{/i}"
    "You took shelter of the tree that you crashed in, but it did not help much.{/i}"
    "{i}Just in a distance, you spot an even bigger tree with a good enough root to handle the rain.{/i}"
    "{i}You run to it in a hurry and take shelter beneath it.{/i}"
    "{i}As soon as you go beneath it, you see a dim light coming from a distance.{/i}"
    m "What is that in the middle of this jungle? A house??"
    "{i}You run towards it to check it out.{/i}"
    scene man_son at bg_fit
    with dissolve 
    with hpunch
    "{i}Infront of you there was a big old warehouse like looking mansion which seemed to be abandoned.{/i}"
    "{i}It had a sort of dark and creepy look, just like some house you would find in a horror movie."
    m "It looks abandoned."
    m "It looks like, It would probably be an old building abandoned by the previous rich owners."
    m "Maybe some noble family of the past lived here."
    "{i}With thoughts like those, you go closer to it for some shelter.{/i}"
    "{i}There are leaks everywhere on the frontyard. You continue to get soaked in the rain.{/i}"
    m "Oh no, I guess I will have to go in or else it will be bad."
    m "I do not think that would be the best choice from me, considering the mystery of this place."
    m "This is giving me very creepy vibes."
    "{i}You could barely feel a small unnatural force calling you from the inside, but you blamed it on your imagination and moved on.{/i}"
    "{i}Ignoring all these warnings, you finally decided to go inside.{/i}"
    m "Let's do this."
    scene main_hall at bg_fit
    with dissolve
    with fade 
    "{i}You were greeted with a big hall like place, with a big chandelieure in the middle hanging down from the ceiling.{/i}"
    "{i}It looked like something long forgotten in the past.{i}"
    "{i}But there was something strange with the house. Once you wandered your eyes, you could see nothing, just 4 rooms behind 4 doors.{/i}"
    "{i}Like a hollow mansion, built for the purpose of just living there, only family without any guests.{/i}"
    "{i}You wonder if that was a sign for the house to be unwelcoming.{/i}"
    "{i}And then you start to wonder, is what youre doing really right? Should you be coming inside this creepy place you do not know of just because of curiosity?{/i}"
    "{i}You start thinking deeply to yourself and had two options now.{/i}"
    "{i}Whether to turn back or stay and explore.{/i}"
    m "What should I do now?"
    menu:
        "Stay and explore.":
            jump label room_room
        "Go back.":
            jump label back_room
label back_room:
    m "I should not do this, I am heading back."
    "{i}As you were saying that, you turn back to the door to go back.{/i}"
    scene black
    "{i}There was nothing. No door at all. Just a wall. The door that you had opened just had disappeared in an instant."
    e "Hush"
    "{i}You heard something in your ear. Something whispering. You did not know what it was. You were alone there.{i}"
    "{i}You panic and start searching for an escape, running as if your life depended on it.{/i}"
    scene backdoor at bg_fit
    with dissolve
    with hpunch
    "{i}You come upon a backdoor and see a lock, with what seemed like animals as a passcode.{/i}"
    m " is this the only escape that I have left?"
    m "I have no idea of what is happening at all, but all that i know is that i need to get out of this place."
    m "I need to go back and start exploring the rooms. There might be some clues there."
    jump room_options
label room_room:
    m "I need to explore this place while waiting for the morning I guess."
    m "Might just find something interesting inside, haha."
    m "How could I sleep when I have this huge thing to explore in front of me."
    m "Adventure is callinggg."
    jump rooom_options
label room_options:
    scene main_hall at bg_fit
    with dissolve
    with fade
    $ hub_visits += 1
    if suspicion >= 15:
        $ caught_reason = "greed"
        jump ending_caught
    if len(rooms_visited) >= 1 and not door_gone:
        call door_vanishes
        scene main_hall at bg_fit
        with dissolve
        with fade
    if suspicion >= 4 and not enc1:
        jump encounter_one
    if suspicion >= 7 and not enc2:
        jump encounter_two
    if suspicion >= 10 and not enc3:
        jump encounter_three
    if suspicion >= 13 and not enc4:
        jump encounter_four

    if suspicion == 0:
        "{i}The chandelier hangs very still.{/i}"
    elif suspicion <= 3:
        "{i}The hall was colder than it was a minute ago. The chandeliers crystals look like theyre shining brighter.{/i}"
    elif suspicion <= 7:
        "{i}Something in the house has noticed you. You feel like the air carries a different weight now.{/i}"
    elif suspicion <= 11:
        "{i}The shadows in the corners have become a bit too thick.{/i}"
    else:
        "{i}The mansion looks like it has stopped pretending. It looks like it is waiting for you to make one more mistake.{/i}"
    if hub_visits == 8:
        "{i}You look strangely at the chandelier as all the crystals suddenly shine at once.{/i}"
        "{i}You blame your drowsiness for seeing things.{/i}"
    menu:
        "You stand in the hallway infront of four rooms that you can explore. Which one will you go to now?"
        "The Kitchen":
            jump kitchen_enter
        "The Laboratory":
            jump lab_eneter
        "The Library":
            jump library_enter
        "The Bedroom":
            jump bedroom_enter
        "Check your phone.":
            jump phone_check 
        "Stop and think about what you know.":
            jump review_progress
        "Go to the back door.":
            if door_gone and symbols_found() == 4:
                jump backdoor_lock
label door_vanishes:
    scene black
    with flicker
    "{i}Far behind you, in the hall that you came by, a door closes. It was like you were a guest and it was showing you away.{/i}"
    m "No, no, no, no."
    "{i}You run. It is the same hall, the same thing hanging from the ceiling, but the front door is simply gone.{/i}"
    "{i}Only a wall, which looked like it was plastered then papered rub against your skin as you felt the door.{/i}"
    e "Hush."
    "{i}The word is breathed into your ear yet again, which felt like it was just the wind but you knew it was something else.{/i}"
    "{i}You turn back. Nothing at all.{/i}"
    "{i}You then go to the far end of the house and see a lock containing 4 animals.{/i}"
    m "That is the way out. That has to be the way out."
    "{i}You check your phone. It said no signal, and the time showed 12:05."
    $ door_gone = True
    return
label review_progress:
    m "Okay, I have got to calm down here. What do I actually have?"
    if "wolf" in clues:
        m "The wolf from the kitchen."
    else:
        m "No wolf yet. Maybe it is in the kitchen."
    if "stag" in clues:
        m "The stag from the laboratory."
    else:
        m "No stag yet. Maybe it is in the laboratory."
    if "owl" in clues:
        m "The owl from the library."
    else:
        m "No owl yet. Probably in the library."
    if "moth" in clues:
        m "The moth from the bedroom."
    else:
        m "No moth yet. That just leaves the bedroom."
    if orders_found() == 4:
        m "And I know all of their orders. Every room told me where its animals stood."
    elif orders_found() == 0:
        m "I do not know the orders of the animals. Every room might hold the piece of that."
    else:
        m "I know where some of the animals stand, but not all of them yet."
    $ tc = len(tokens)
    if tc>0:
        m "And I am carrying [tc] small things that someone in this house had wanted me to have."
    jump room_options

label phone_check:
    $ phone_checks += 1
    if phone_checks == 1:
        "{i}You pull out your phone. The clock has the same time as before and it has no signal.{/i}"
        "{i}All that you can see is the fourteen missed calls from Mira whom you cannot answer due to the signal.{/i}"
        "{i}Mira was your sister who had been working hard for your family since your mom died years ago.{/i}"
        $ lore.add("phone_1")
    elif phone_checks == 2:
        "{i}The screen lights up on its own and you see a voicemail that you had never opened.{/i}"
        mira "Hello, it is me. I know that you are busy. I found mom's soup recipe. It was awful. Probably it was I who didnt know how to make it."
        mira "Come home sometime. Lets cook it together. Bye."
        "The recording ends."
        $ lore.add("phone_2")
        $ suspicion += 1
    elif phone_checks ==  3:
        "This time, the phone calls Mira by itself. The ring goes despite there being no signal."
        "She answers. But there was no voice. Maybe you could not hear what she was saying."
        e "Who is that?"
        "Your body suddenly feels the chill. It came and went again."
        e "Who is that waiting for you?"
        e "Everyone has someone...waiting."
        $ suspicion += 1
    else:
        "{i}You hold the phone but do not open it. You already knew what it would say.{/i}"
        jump room_options
label encounter_one:
    $ enc1 = True 
    "{i}Above you, the chandelier starts to shake. It slowly lightens itself one at a time.{/i}"
    "{i}For a moment, you feel like the house felt like what it was meant to be.{/i}"
    e "Welcome."
    "{i}A child's voice, you notice until you feel the layers underneath it, like it was coming from the well.{/i}"
    e "I dont feel lonely here anymore."
    menu:
        "How do you intend to answer?"
        "Answer polietely.":
            m "Thank you... It is a lovely house."
            e "haha, make yourself at home..."
            "Manners,, seem like it is the currency here."
        "Demand to be let out.":
            m "Let me out. Right now."
            e "haha, youre like everyone else."
            $ suspicion += 1
        "Say nothing.":
            "{i}You say nothing. The candle burns out eventually and then it returns to normal.{/i}"
    jump room_options
label encounter_two:
    $ enc2 = True
    "{i}Somewhere around the house, you feel a ball bouncing slowly and evenly.{/i}"
    "{i}It comes slowly to you, a wooden ball from the empty hall and stops at your shoe.{/i}"
    "{i}It is painted with blue color and is chipped at one side. The blue paint seems to be resembling a name, LENORA.{/i}"
    menu:
        "What do you do with the ball?"
        "Roll it gently back into the dark.":
            "{i}You crouch down and push it slowly the way back it came. You could not hear anything.{/i}"
            "{i}But a moment later, what sounded like a pleased sound came from the dark.{/i}"
            "{i}It almost sounded like a breath of laughter.{/i}"
            fd "Again?"
            m "{i}Not now. But thank you very much.{/i}"
            "{i}The hall felt, slightly bit less crowded for a bit.{/i}"
            $ lore.add("ball")
        "Kick it away.":
            "{i}You put your boot to it and send it clattering into the dark.{/i}"
            $ suspicion += 2
            fd "That was mine..."
            "{i}The words sounded small, and wounded.{/i}"
        "Pocket it.":
            "{i}You take it. It is heavier than what a wooden ball should be.{/i}"
            $ suspicion += 2
            e "Put that back."
            m "You felt fear. You immediately put it back."
    jump room_options
label encounter_three:
    $ enc3 = True
    scene black 
    with flicker
    "{i}Your phone rings inside your pocket.{/i}"
    "{i}No signal, it says. But the text Mira appears on the screen.{/i}"
    "{i}It rings anyways.{/i}"
    menu:
        "The screen reads: Mira"
        "Answer it.":
            m "Mira?"
            mira "Hey, it is me. Where are you right now? You said you would be home."
            "{i}It sounded exactly like her. It was the cruelest thing that you have eer heard.{/i}"
            mira "Why wont you ever come home?"
            mira "Do you hate it here?"
            m "{i}This is not her. This is not her. This is not her....this is not her.{/i}"
            "{i}The voice slides mid word.{/i}"
            e "That is what I want too. Dont you see that we are alike?"
            $ suspicion += 1
        "Let it ring.":
            "{i}You left the phone in your pocket and let it ring, ring and then ring.{/i}"
            "{i}This is exactly what you have done for 2 years, and your shame burns brighter than ever before.{/i}"
            "{i}It eventually stops. A voice then, which you had never heard before, says kindly...{/i}"
            e "You are very good at that. Letting it ring like that."
            m "Shut up."
            e "I am not judging. I am just saying that I woukd have answered."
        "Throw the phone across the wall.":
            "{i}It cracks on the plaster then the screen goes white, then black. The ringing does not stop.{/i}"
            $ suspicion += 2
            e "Oh, that was her number. She will be sad if she cannot reach you."
    scene main_hall at bg_fit
    with dissolve 
    with fade
    jump room_options
label encounter_four:
    $ enc4 = True
    "{i}The walls begin to breathe.{/i}"
    "{i}There is no other word for it. The wallpaper swells an sinks back like the chest of something asleep.{/i}"
    "{i}All four doors swing open at once. Behind each one is the same dark matter Which starts leaning towards you.{/i}"
    e "You have touched so much of my things."
    e "I dont want to be angry. I am tired."
    e "If you keep taking from me, I will have to keep you."
    menu:
        "You have one clear moment. What do you do?"
        "Run for the back door." if symbols_found() == 4:
            "{i}You run. The hall stretches under your feet and snaps you back infront of the lock.{/i}"
            jump backdoor_lock
        "Apologise. Mean it.":
            m "I am sorry. I did not understand what any of this was."
            m "I will be careful from now. I promise."
            e "Promises... You people and your promises."
            "{i}The walls slow their breathing. One by one, the doors drift shut. It is not forgiveness, but a pause.{/i}"
            $ suspicion -= 2
            jump room_options
        "Stand your ground and look at it.":
            "{i}You turn to the dark at the far end of the hall and make yourself keep your eyes open.{/i}"
            "{i}You stare far back into the hall.{/i}"
            "{i}Something tall stands there. Not really a shape, but more like the absence of one.{/i}"
            "{i} It does not move. It only lets you see that it is there.{/i}"
            $ lore.add("glimpse")
            $ suspicion += 1
            e "Brave or foolish, it is hard to tell the difference."
    jump room_options
label kitchen_enter:
    scene kitchen at bg_fit
    with dissolve
    with fade
    if "kitchen" not in rooms_visited:
        $ rooms_visited.add("kitchen")
        "{i}You push the door open, and the smell reaches you before the sight does.{/i}"
        "{i}Something sweet that had gone sour, like rotten fruits.{/i}"
        "{i}There was a long table down the road, possibly for five or six people. Only one was spotless.{/i}"
        m "Someone had set this table and never got to sit on it."
    else:
        "{i}The kitchen is exactly how you had left it. The pot ws still steaming.{/i}"
        jump kitchen_menu
label kitchen_menu:
    menu:
        "What do you want to check?"
        "The long table.":
            jump kitchen_table
        "Sit in the sixth chair." if "k_table" in done and "k_sit" not in done:
            jump kitchen_sit
        "The knives and the cutting board.":
            jump kitchen_knives
        "The window":
            jump kitchen_window
        "The stove and steaming pot":
            jump kitchen_stove
        "The tin on the high shelf.":
            jump kitchen_tin
        "The pantry.":
            jump kitchen_pantry
        "The recipe book.":
            jump kitchen_recipe
        "The cellar door." if "k_key" in done:
            jump kitchen_cellar
        "The cellar door." if "k_key" not in done:
            "{i}A heavy iron bolt and a lock. It will probably want a key first."
            jump kitchen_menu
        "Leave the kitchen.":
            jump room_options
label kitchen_table:
    "{i}Only the sixth chair had been polished. A small card was there which stated, for our guest.{/i}"
    if "k_key" in done:
        m "{i}The card has not change and it still says guest.{/i}"
        jump kitchen_menu
        "{i}The handwriting is a little shaky.{/i}"
        menu:
            "What do you do?"
            "Lift the sixth plate.":
                "{i}Under it sits a small brass key, pressed into the wood as if the table had grown it.{/i}"
                $ done.add("k_key")
                $ done.add("k_table")
                m "Someone wanted me to find this."
            "Leave the plate alone.":
                $ done.add("k_table")
                "{i}Something about that one clean plate makes your skin crawl. Maybe you should check it next time."
                jump kitchen_menu
label kitchen_sit:
    $ done.add("k_sit")
    "{i}You pull out the sixth chair and sit. It fits you perfectly like it was made for you.{/i}"
    "{i}For a moment, you wonder if it was actually made for you, but you discard thise thoughts immediately.{/i}"
    "{i}Steam begins to rise from the pot. Ginger and cinnamon, clear broth with something floating on it.{/i}"
    "{i}Your mothers soup{/i}"
    "{i}Your mother used to make it for you every sunday during childhood.{/i}"
    m "{i}I have never made it since the funeral. It is always Mira that makes it.{/i}"
    e "Eat, if you would like. No one has to eat alone here."
    menu:
        "The spoon rests besides your hand."
        "Dont eat, say thanks and then stand up.":
            m "Thank you. It smells wonderful but I cannot stay."
            "{i}The steam hangs on for a moment, and then thins to nothing. You have the odd impression of someone nodding.{/i}"
            e "...Most of them eat."
            $ lore.add("k_sit")
        "Pick up the spoon.":
            "{i}The moment the spoon touches your lip, the broth burns to ash.{/i}"
            "{i}The ash to dust and that to a cold which runs straight down your throat.{/i}"
            $ suspicion += 3
            e "Oh, now you've started."
            "{i}You gag and shove yourself back. The chair slides away on its own though, letting you leave.{/i}"
            "{i}You get the dreadful feeling of having signed something.{/i}"
            jump kitchen_menu
label kitchen_knives
    "{i}Every knife is oiled and bright, but the cutting boards are scarred from decades ago.{/i}"
    "{i}Carved into one corner was a wolf's head with its jaw half open.{/i}"
    if "wolf" not in clues:
        $ clues.add("wolf")
        m "A wolf. That is the first of the four animals on the lock."
    else:
        m "The wolf again. I have already got that one."
    jump kitchen_menu
label kitchen_window:
    "{i}The rain runs down in the kitchen wimdow. Beyond it there is a garden like looking place."
    if "k_window" in done:
        m "Four graves, and one hole. One hole, waiting? I do not want to look at it again."
    else:
        $ done.add("k_window")
        $ lore.add("k_window")
        m "Wow, four stones there, four rooms and four animals, and there is a fifth hole dug up."
        m "Maybe it is just soil. It doesnt mean anything.{/i}"
        "{i}You look closer. The fifth hole looks exactly like your height.{/i}"
        jump kitchen_menu
label kitchen_stove:
    "A crooked wooden lid stays on the pot upon the stove and there was a wooden spoon on the side too."
    if "k_stove" in done:
        m "The pot is quiet now. I will not wake it again."
        jump kitchen_menu
    menu:
        "What do you do?"
        "Settle the lid straight and turn the dial to off.":
            $ done.add("k_stove")
            $ lore.add("k_stove")
            "{i}You set the lid straight and turn the dial to off. It sets to OFF even though nothing was ever lit.{/i}"
            "{i}The steam thins and somewhere very faintly, it lets out a long breath like noise identical to a person.{/i}"
            fa "...thank you, dear."
            "{i}It is the first voice in the house that has not frightened you.{/i}"
        "Lift the lid and look inside.":
            $ done.add("k_stove")
            "{i}Inside is clear broth, perfectly still. A dead moth is on the surface of the liquid.{/i}"
            $ suspicion += 1
            "{i}As you watch it, it's wings twitch.{/i}"
            m "{i}Okay, no. The lid goes back.{/i}"
        "Leave it be.":
            "{i}Some pots are best left to simmer.{/i}"
    jump kitchen_menu
label kitchen_tin:
    if "k_tin" in done:
        m "{i}I have already dealt with this tin.{/i}"
        jump kitchen_menu
    "{i}A biscuit tin painted with roses. Please ask first is carved carefully there.{/i}"
    menu:
        "What do you do?"
        "Ask out loud, if you may open it.":
            m "Excuse me. May I? I would like to see what is inside. I will be careful."
            "{i}The silence stretches. Then the padlock opens itself and drops into your palm.{/i}"
            "{i}Inside, there wasa plain gold ring worn thin and and a note that said : Whoever comes to the table, do not let the pot go cold.{/i}"
            $ tokens.add("ring")
            $ done.add("k_tin")
            $ lore.add("k_tin")
            m "Her wedding ring. She left it for a stranger."
            fa "Strangers are the only ones who stay for a little while, dear. Everyone else is gone."
        "Pry it open with a kitchen knife":
            "{i}It snaps like the crack of a bone. The gold ring rolls across the floor under the stove where something quick catches it.{/i}"
            $ suspicion += 2
            $ done.add("k_tin")
            e "She asked you to ask."
            m "{i}Great. So thats gone.{/i}"
        "Leave it. It is not yours.":
            "{i}You leave it where it sits. It feels like the first right decision that you have made tonight.{/i}"
    jump kitchen_menu
label kitchen_pantry:
    "{i}The pantry door was swollen with damp and groans as it gives.{/i}"
    "{i}There were medicines for cough, headaches, fever and nerves."
    "{i}Rows and rows of that last one."
    if "k_pantry" in done:
        m "I have seen enough of this pantry."
        jump kitchen_menu
    $ done.add("k_pantry")
    $ lore.add("k_pantry")
    "{i}On the highest shelf, you could see a single jar wrapped in cloth tied with a blue hair ribbon.{/i}"
    menu:
        "Do you take it down?"
        "Take it down and read the label.":
            "For when she asks to come home."
            "{i}The jar is warm and you can even feel it humming faintly.{/i}"
            $ suspicion += 2
            e "Put that back."
            "{i}You immediately put it back. Your hand shakes so badly that it chatters against the shelf.{/i}"
        "Leave it where it is.":
            "{i}You close the pantry quietly. Some hopes should be left to rest.{/i}"
            jump kitchen_menu
label kitchen_recipe:
    "{i}A thick, stained book lies in the stove. Most of the pages look ordinary."
    if "o_wolf" in clues:
        m "{i}I have read it. I know where she put herself.{/i}"
        jump kitchen_menu
    "{i}Then the margins change and the measurements stop making sense.{/i}"
    "{i}Beneath it, there was a line underlined so hard the pen tore the paper.{/i}"
    "'Forgive me, my loves. I onl wanted to keep us together.'"
    $ clues.add("o_wolf")
    $ lore.add("k_recipe")
    m "Last, fourth. SEraphin, the wolf took the last place of all."
    jump kitchen_menu
label kitchen_cellar:
    if "k_cellar" in done:
        m "{i}No, I have been down once. That is enough.{/i}"
        jump kitchen_menu
        "{i}The key turnsvery easily"

        
        







    

            






