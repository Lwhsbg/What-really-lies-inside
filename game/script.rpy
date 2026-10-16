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
    "{i}You took shelter of the tree that you crashed in, but it did not help much.{/i}"
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
            jump room_room
        "Go back.":
            jump back_room
label back_room:
    m "I should not do this, I am heading back."
    "{i}As you were saying that, you turn back to the door to go back.{/i}"
    scene black
    "{i}There was nothing. No door at all. Just a wall. The door that you had opened just had disappeared in an instant."
    e "Hush"
    "{i}You heard something in your ear. Something whispering. You did not know what it was. You were alone there.{i}"
    "{i}You panic and start searching for an escape, running as if your life depended on it.{/i}"
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
    jump room_options
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
            jump lab_enter
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
label kitchen_knives:
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
        m "{i}Maybe it is just soil. It doesnt mean anything.{/i}"
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
    "{i}The key turns very easily, like it had been awaiting to.{/i}"
    "{i}It carried the smell of earth and apples.{/i}"
    menu:
        "Go down?"
        "Go down.":
            $ done.add("k_cellar")
            scene black
            with fade_black
            "{i}The stairs go a long way down.{/i}"
            "{i}At the bottom, there are shelves of preserves and racks of coats.{/i}"
            "{i}Pinned to a small blue coat is an envelope in a man's hand.{/i}"
            "'To whoever stays the longest:'"
            "{i}Inside is a single page.{/i}"
            "'I did not understand what I was asking when I asked it. I thought love was a door I could hold open. It is a hand that I cannot let go of.'"
            "'If you are reading this, then you have already been counted. Forgive her. She is not cruel, but just afraid of the quiet.'"
            $ lore.add("k_letter")
            m "Forgive who? THe mother? The daughter? The thing that answered?"
            "{i}At the far end of the cellar, you then see a small door.{/i}"
            menu:
                "Do you open it?"
                "Open the small door":
                    "{i}Behind it is a room which is no bigger than a cupboard. A ring of chalk on the floor, and a child's tin cup.{/i}"
                    "{i}And the wall there was scratched with chalk multiple times too. Over and over, the same sentence.{/i}"
                    "SHE ASKED FOR A LITTLE WHILE"
                    $ suspicion += 3
                    $  lore.add("k_ritual_room")
                    e "That is where I woke up."
                    "{i}You run. The door slams on your fingers as you race with your heart on climbing up those long stairs of the cellar.{/i}"
                "Leave it shut.":
                    "{i}You do not bother with that door.{/i}"
            scene kitchen at bg_fit
            with dissolve
            with fade
        "Stay at the top.":
            "{i}You shut the cellar and then step back. Whatever is inside there can keep on waiting.{/i}"
            jump kitchen_menu
label lab_enter:
    scene lab at bg_fit
    with dissolve
    with hpunch
    if "lab" not in rooms_visited:
        $ rooms_visited.add("lab")
        "{i}As soon as you enter the lab, you can smell the chemicals and a small electrical hum can also be heard.{/i}"
        "{i}There are cracked glasswares , a brass microscope, a cabinet  with dial lock.{/i}"
        "{i}But the most obviouslt noticeable of all, in the middle there was a heavy oak chair with leather straps for every limb.{/i}"
        m "The hum is probably from the pitch of a heart monitor in a quiet room."
        m "Your stomach turns over after imagining what might have possibly happened here."
        jump lab_menu

label lab_menu:
    menu:
        "What do you want to check?"
        "The journal on the desk.":
            jump lab_journal
        "The skull on the wall":
            jump lab_skull
        "The restraint chair":
            jump lab_chair
        "The humming machine.":
            jump lab_machine
        "The microscope.":
            jump lab_microscope
        "The locked cabinet." if "l_code" in clues:
            jump lab_cabinet
        "The locked cabinet." if "l_code" not in clues:
            "It seems to be a heavy cabinet with a dial which you do not know the code of, yet. Maybe you will find it."
            jump lab_menu
        "Leave the laboratory.":
            jump room_options
label lab_journal:
    "{i}The journal is covered in green cracked leather.{/i}"
    if "o_stag" in clues:
        m "{i}I know what is in it. I dont need to read it twice.{/i}"
        jump lab_menu
    "{i}The first entries about a doctor trying to cure a young girl with fever is quite good.{/i}"
    "{i}He seems clever enough to fix it.{/i}"
    "{i}But the journal gets scribbled more and more and gets messed up until the last page.{/i}"
    "{i}The last page has no words at all. Only a sketch of dial with three numbers circled: 4, 2, 9{/i}"
    $ clues.add("l_stag")
    $ clues.add("o_stag")
    $ clues.add("l.code")     
    $ lore.add("l_journal")
    m "I got the code for the dial finally..."
    jump lab_menu
label lab_skull:
    "{i}Mounted above the cabinet, antlers spread wide across the wall, is a stag's skull.{/i}"
    "{i} Something shook faintly in one of the antlers.{/i}"
    if "stag" not in clues:
        $ clues.add("stag")
        m "Stag. That is the second animal, in the same style as the wolf."
        "{i}There ws something carved in the bone beneath it.{/i}"
        "'Papa was always so proud of this boy.'"
    else:
        m "The stag again. I have already got this one."
    jump lab_menu
label lab_chair:
    "{i}The chair is old oak, with leather straps at the wrist, ankles and the chest.{/i}"
    if "l_chair" in done:
        m "{i}I have already done what I can here.{/i}"
        jump lab_menu
    "{i}Under the seat, someone has scratched four tally marks with a fingernail. The fifth mark is half finished.{/i}"
    menu:
        "What do you do?"
        "Unbuckle the straps, one by one.":
            $ done.add("l_chair")
            "{i}You kneel and undo the buckles slowly, and it sounds like the leathers sighed, strap by strap.{/i}"
            "{i}When the last one snaps, something small slides outside.{/i}"
            "{i}It was a silver pocket watch, paused at 4:29.{/i}"
            $ tokens.add("watch")
            $ lore.add("l_chair")
            fb "She never struggled as much as I saw her."
            "{i}The voice sounds like it was of a man's, hoarse.{/i}"
            "{i}It had already gone away befor you could answer.{/i}"
        "Sit in and strap yourself.":
            "{i}You lower yourself into the seat. The oak was warm and the straps buckle slowly around you.{/i}"
            "{i}The hum from the machine a bit far away gets louder.{/i}"
            "{i}You try to break free, until the skin scrapes off your hands and knees, and strap free.{/i}"
            $ suspicion += 2
            $ done.add("l_chair")
            e "Wasnt it dreadful? haha."
            m "{i}Whatever happened in this room, it was nothing about the cure.{/i}"
        "Leave it alone.":
            "{i}You do not touch the chair. Maybe it is better left alone.{/i}"
label lab_machine:
    "{i}Behind the machine is what looks like a dial valve. It is the source of the hum.{/i}"
    if "l_machine" in done:
        "{i}I have had my time with this machine already. I don't want to see it again.{/i}"
        jump lab_menu
    $ done.add("l_machine")
    menu:
        "Rest your hand on top of the machine?"
        "Rest your hand on it.":
            scene black
            with flicker
            "{i}The hum climbs into your arm, and the room drops away.{/i}"
            "{i}You feel something like a mother's hand resting gently in  yours, thin like paper.{/i}"
            "{i}Your phone buzzes in your pocket. It sounded like it was a message from work.{/i}"
            "{i}Two minutes, mom.{/i}"
            "{i}You make a quick call and return.{/i}"
            "{i}By the time you reach back, she was surrounded by the nurses already. She was no more.{/i}"
            $ memories.add("hospital")
            scene lab at bg_fit
            with dissolve
            with fade 
            "{i}Your hand is still on the machine. Your face is wet from the sweat.{/i}"
            e "You stepped out of the room too..."
            e "Well, I do know what being left in a room feel like."
            menu:
                "What do you say?"
                "I had no idea it was the last time..":
                    e "Nobody does."
                    "{i}The hum drops a little.{/i}"
                    $ suspicion -= 1
                "It was not my fault.":
                    m "It was not my fault. I had done nothing wrong."
                    e "Of course not."
                    m "The tone was so soft that it sounded eerie."
                    $ suspicion += 1
                "Don't say anything.":
                    "{i}You pull your hand back from the machine. Some memories are better left alone.{/i}"
            $ done.discard("lab_menu")
            jump lab_menu
label lab_microscope:
    "{i}A brass microscope stands on the bench.{/i}"
    if "l_scope" in done:
        m "I have looked. I am never looking back again."
        jump lab_menu
    $ done.add("lab_scope")
    "{i}You press your eye on the microscope.{/i}"
    "{i}It was a bit blurry at first, but it started clearing up.{/i}"
    "{i}You can see a warm light flickering, going off and on.{/i}"
    "{i}Almost like a heartbeat.{/i}"
    $ lore.add("l_scope")
    m "That's her. That is her. Somebody put a lttle girl under the glass. "
    "{i}The walls around the laboratory ruffle a bit.{/i}"
    jump lab_menu
label lab_cabinet:
    if "l_cabinet" in done:
        m "{i}The cabinet is empty and open now.{/i}"
        jump lab_menu
    $ done.add("l_cabinet")
    "{i}You turn the dial and put the code that you found out.{/i}"
    "{i}Inside, there was something that looked like a family photo.{/i}"
    "{i}A tall man and a woman with her sleeves rolled up. A girl with a gap on her teeth and a moth in a finger, and a little boy with a book.{/i}"
    "{i}There creepily seemed to be a space for the fifth.{/i}"
    e "I like that one. Everybody looks so happy in it."
    $ suspicion += 1
    jump lab_menu
label library_enter:
    scene library at bg_fit
    with dissolve
    with fade
    if "library" not in rooms_visited:
        $ rooms_visited.add("library") 
        "{i}The library was dark and huge, with shelves everywhere with books, which looked like it had not been dusted in decades.{/i}"
        "{i}You could see a fireplace and a portrait above it, besides a reading desk."
        m "If this place can explain itself anywhere, It would be here."
    else:
        "{i}The library is silent and patient.{/i}"
    jump library_menu

label library_menu:
    menu:
        "What do you want to check?"
        "The ledger on the reading desk.":
            jump library_ledger
        "The owl bookend.":
            jump library_owl
        "The book on the floor.":
            jump library_book
        "The portrait above the fireplace.":
            jump library_portrait
        "The ashes in the fireplace.":
            jump library_fireplace
        "The turning globe.":
            jump library_globe
        "Search the shelves." if "shelf_note" not in clues:
            "{i}There are hundreds of books here. There is no way you would find something specific.{/i}"
            jump library_menu
        "The hidden book in the shelves." if "shelf_note" in clues:
            jump library_hidden
        "Leave the library.":
            jump room_options
label library_ledger:
    "{i}A heavy ledger lies open on the desk, names and dates in the fading ink. Alaric, Seraphine, Caspian and Lenora.{/i}"
    if "shelf_note" in clues:
        m "I have already copied the margin note. Third shelf, fourth row and third book."
        jump library_menu
    "{i}Below each name is a little numerical text with hidden written over it.{/i}"
    "{i}You read the hint carefully. 3,1,4.{/i}"
    m "So third shelf, fourth row and the third book."
    $ clues.add("shelf_note")
    $ lore.add("l_ledger")
    m "All four of them dies in four months? I wonder what even could happen for that to occur."
    jump library_menu
label library_owl:
    "{i}In the corner of the desk, there seemed to be an owl carved from dark wood, with it's eyes hollowed out.{/i}"
    if "owl" not in clues:
        $ clues.add("owl")
        m "An owl. So that is the third creature. It thas a similar style of carving as the others."
        $ lore.add("owl")
    else:
        m "The owl again. I have already got this one."
        jump library_menu
label library_book:
    "{i}The book on the floor is open, which looked like it was dropped in the past never to be picked up again.{/i}"
    if "l_book" in done:
        m "{i}It is back in the shelf now. That is better.{/i}"
        jump library_menu
    menu:
        "What do you do?"
        "Close it gently and then put it back on it's shelf.":
            $ done.add("l_book")
            "{i}You straighten the crumbled pages, gently pick up the book and close it then put it back on its shelf.{/i}"
            "{i}The rough book fits very smoothly and comfortably into the shelf, like it had been waiting for years.{/i}"
            "{i}After you kept the book on it's shelf, something flutters out. Which looks like a green ribbon{/i}"
            "{i}It felt like a gift to you so you keep it.{/i}"
            $ tokens.add("bookmark")
            fc "Please be careful in the library."
            "{i}That sounded like a little boy's voice, embarasses and then gone in a second.{/i}"
        "Skim it, then toss it aside.":
            "{i}Poems, mostly whch seemed to be written by a pencil.{/i}"
            "{i}You toss it back on the floor figuring it was where it belonged.{/i}"
            $ suspicion += 1
            e "He loved that one."
            "{i}A fluttering noise comes from the other side of the library like some startled bird then goes quiet.{/i}"
            m "What was that?"
        "Tear out a page.":
            "{i}You look at it and tear up a page. The tearing page does not sound like paper at all.{/i}"
            "{I}It sounded like a sharp, small cry which a small kid would make.{/i}"
            $ suspicion += 2
            e "no.. not his books..."
            "{i}The page crumbles into ash in your hands and the library grows colder, almost quieter.{/i}"
            jump library_menu
label library_portrait:
    "{i}Above the fireplace sits a huge portrait, of the family photo that you saw in the laboratory, but this time painted in a far finer detail."
    "{i}The one wth the father, mother, the daughter and the son, also detailing the moth on the little girl's hands.{/i}"
    "{i}The painter has left the room. There is an empty chair at the end of the group, painted faintly.{/i}"
    "{i}Though it looked like it was added in the last minute and unfinished.{/i}"
    if "l_portrait" in done:
        m "{i}don't look at the empty chair, don't look at the empty chair...{/i}"
    else:
        $ done.add("l_portrait")
        $ lore.add("l_portrait")
        m "{i}They expected someone...they have always been expecting someone.{/i}"
        "{i}As you step back, you came to notice that the little girl no longer seemed to be looking at the painter like she did in the photo before.{/i}"
        "{i}She is looking out of the frame. At you.{/i}"
    jump library_menu
label library_fireplace:
    "{i}The fireplace is cold, the ashes just grey crust now.{/i}"
    "{i}You crouch and sift gently.{/i}"
    "{i}Most of it crumbles at your touch, but a few curled fragmented pieces of paper survive at the back.{/i}"
    if "l_fire" in done:
        m "There is nothing else here."
        jump library_menu
    menu:
        "Do you try to read them?"
        "Piece the fragments together.":
            $ done.add("l_fire")
            "{i}A handful of words manage to survive.{/i}"
            "'...It cannot be undone. The binding holds four of us, but the thing that answered is not her. It only wears her loneliness like a coat...'"
            "'If it ever goes outside of this house, it will go looking for more of us.'"
            $ lore.add("l_fire")
            $ suspicion += 1
            m "{i}It is not Lenora. It is something that put on her loneliness, and the family have spent a century holding it in.{/i}"
            "{i}Behind you, you can feel the irons rattle in their places, though there was nothing there to touch them.{/i}"
        "Leave them.":
            "{i}You brush the soot from your hands. You imagine the ashes will not be worth it.{/i}"
            jump library_menu
label library_globe:
    "{i}You lay a palm on the turning globe as it stops at once, as if it was relieved.{/i}"
    "{i}The continents which are present in the globe were old and wrong. But around the house in an unmarked forest, there were two pins.{/i}"
    "{i}One was a big gold pin and one was a smaller red one.{/i}"
    if "l_globe" in done:
        m "The red pin is where I crashed. I know, I know."
        jump library_menu
    $ done.add("l_globe")
    $ lore.add("l_globe")
    $ suspicion += 1
    m "{i}That looks exactly like where I went off the road. The red pin...{/i}"
    m "{i}Somebody marked it... before I even got here.{/i}"
    m "{i}I had just changed my tires. The steering had not failed either. Something took it.{/i}"
    e "{i}I mark the road for everyone, most just go quietly.{/i}"
    "{i}The globe begins to spin again now, faster than before.{/i}"
    jump library_menu
label library_hidden:
    if "o_owl" in clues:
        m "{i}The book is back to where it was, and I know what it says.{/i}"
        jump library_menu
    m "{i}Third shelf, fourth row and the third book from there.{/i}"
    "{i}You pick up the book. It matches none of it's neighbouring books.{/i}"
    "{i}It did not have any dust. It had no title in it either.{/i}"
    "{i}Inside is a diary in a boy's little hand. The one that the boy seemed very protective and careful about.{/i}"
    "{i}'Father says that my turn is in the second. Lenora is going first. Maybe she has already gone. Maybe I hould read to her so she does not get scared.'{/i}"
    "{i}I read to her every night. The same two books. She laughs in the same places, even now.{/i}"
    $ clues.add("o_owl")
    $ lore.add("l_diary")
    "{i}You think of Mira, when she was eight curled up against your arm when you would read her the same picture book.{/i}"
    "{i}She would laugh at the same part everytime, no matter how much you read to her.{/i}"
    "{i}The last time that you were home, Mira had joked about if you could read her the picture book again.{/i}"
    "{i}You said that you were busy. She then had laughed, like it did not matter at all.{/i}"
    $ memories.add("mira_book")
    m "{i}Second. Caspian went second. Because he wanted his sister not to be afraid.{/i}"
    e "He read it to her until the very end. He was so good at it."
    "{i}The diary slips from your hands. You do not feel your fingers let go. It was already gone before it reaches the floor.{/i}"
    jump library_menu
label bedroom_enter:
    scene bedroom at bg_fit
    with dissolve
    with fade
    if "bedroom" not in rooms_visited:
        $ rooms_visited.add("bedroom")
        "{i}Unlike any other houses, the bedroom actually felt cared for. A small bed sits made, and a music box rests on the night stand.{/i}"
        "{i}A vanity mirror stands in the corner.{/i}"
        "{i}On the dresser, there was a glass case of pinned moths and on the table by the window, a dollhouse which was the perfect copy of this very house.{/i}"
        m "{i}It feels like someone still comes to this room every night.{/i}"
        "{i}You cannot see anything outside from the window. It only gives you your own tired face.{/i}"
    else:
        "{i}The little room is quiet. The covers on the bed look like they were freshly smoothed.{/i}"
        jump bedroom_menu
label bedroom_menu:
    menu:
        "What do you want to check?"
        "The moth case on the dresser.":
            jump bedroom_case
        "The little bed.":
            jump bedroom_bed
        "The music box.":
            jump bedroom_musicbox
        "The vanity mirror.":
            jump bedroom_mirror
        "The dollhouse.":
            jump bedroom_dollhouse
        "The marks on the door frame.":
            jump bedroom_frame
        "The loose floorboard." if "b_mirror" in done:
            jump bedroom_floorboard
        "Look for what the mirror showed." if "b_mirrror" not in done:
            "{i}Nothing about the floor looks out of place. You would need a reason to look closer.{/i}"
            jump bedroom_menu
        "Leave the bedroom.":
            jump room_options
label bedroom_case:
    "{i}Moths, dozens of them, pinned neatly under the glass with their wings spread wide. Each one has a label with a name on it.{/i}"
    if "moth" not in clues:
        $ clues.add("moth")
        m "A moth. That must be the fourth. Now that is finally all four animals for me."
        $ lore.add("b_case")
        "{i}One of the moths, you swear, was not pinned into position a moment ago.{/i}"
    else:
        m "The moth again. I have already got this one."
        jump bedroom_menu
label bedroom_bed:
    "{i}The bed is made with hospital-sharp corners and the pillow is plumped. The blanket is folded back as if someone is about to climb in.{/i}"
    if "b_bed" in done:
        m "{i}She is sleeping. Let her sleep.{/i}"
        jump bedroom_menu
    menu:
        "What do you do?"
        "Straighten the blanket, and say goodnight to the empty bed.":
            $ done.add("b_bed")
            "{i}You draw the blanket up to the pillow and smooth it flat. It feels stupi, but feels useful somehow too.{/i}"
            m "Goodnight. I hope it is quiet for you."
            "{i}The matress sighs, and what sounds like a child makes a long, sleepy breath."
            "{i}On the empty pillow which was there a moment ago, there is a small moth with a crooked wing and two uneven eyes.{/i}"
            "{i}You take the moth.{/i}"
            $ tokens.add("moth_toy")
            $ lore.add("b_bed")
            fd "Mothy takes the scary away. You can borrow him."
            "{i}Your throat becomes tight. You think of every bedtime you did not stay up for Mira.{/i}"
            $ memories.add("mira_goodnight")
        "Sit on the edge of the bed.":
            "{i}The matress dips under your weight, and it is very warm.{/i}"
            "{i}It doesnt feel like the warmth of a place where someone had slept though.{/i}"
            "{i}It feels more like a place where someone is still lying. Just under the blankets, but out of sight.{/i}"
            "{i}The mattress tips very slightly toward the pillow as though a second weight has settled besides you.{/i}"
            $ suspicion += 2
            $ done.add("b_bed")
            m "{i}Don't move. Do not turn your head....{/i}"
            e "Stay.. just until I fall asleep."
            "{i}A cool hand rests gently on yours, light as a paper, then it is gone.{/i}"
            "{i}You stumble upon your feet without even realizing that you were standing.{/i}"
        "Step away from it":
            m "Whatever this bed it waiting for, it is not me."
            jump bedroom_menu
label bedroom_musicbox:
    "{i}A small music box sits on the nightstand, with a lid that is carved using tiny moths. It looks like the key there is stiff with age.{/i}"
    if "b_music" in done:
        m "{i}The tune is still in my head. I cannot stop imagining it.{/i}"
        jump bedroom_menu
    menu:
        "What do you do?"
        "Wind it, and let it play all the way through.":
            $ done.add("b_music")
            "{i}It clicks, stutters and begins.{/i}"
            "{i}You know it. You know it the way that you know your own name. It was the same lullaby you used to hum it to Mira when she was a kid and afraid of the dark.{/i}"
            "{i}You had never asked yourself where you had learned it though.{/i}"
            $ memories.add("lullaby")
            $ lore.add("b_music")
            m "{i}Mom sang this to us. The both of us. That is how i knew of it...{/i}"
            "{i}Then from somewhere in the walls, a second voice begins to hum along, which sounds like a mother's voice.{/i}"
            fa "She always did hum it a little sharp."
            "{i}The box winds down. The last note hangs in the air for a long time after the box had turned off."
            $ suspicion -= 1
        "Slam the lid shut.":
            "{i}You snap the lid back down mid note.{/i}"
            "{i}The music box shrieks and something inside the wall begins to sob.{/i}"
            $ suspicion += 2
            $done.add("b_music")
            e "That was hers."
        "Leave it be.":
            "{i}You leave the key where it was thinking it was not your playlist to listen to.{/i}"
            jump bedroom_menu
label bedroom_mirror:
    "{i}The vanity mirror is fogged thick with age. You wipe it clear using your sleeve and for a fraction of second, it seemed like your reflection was really not your own.{/i}"
    "{i}Behind you stood a young girl in a nightgown, probably nine, holding a candle.{/i}"
    "{i}Her face is just a smear of shadow.{/i}"
    "{i}She raises one finger to her lips, shh. Then points it at the foot of the bed.{/i}"
    if "b_mirror" not in done:
        $ done.add("b_mirror")
        $ suspicion += 1
        $ lore.add("b_mirror")
    "{i}You spin around. Nothing there. When you look back, it is only you again, pale and now shaking.{/i}"
    m "{i}She wanted me to look at the foot of the bed.{/i}"
    jump bedroom_menu
label bedroom_dollhouse:
    "{i}To your absolute surprise, the dollhouse is an exact copy of the mansion: Four rooms and a hall, with every detail done perfectly.{/i}"
    "{i}Even the chandelier.{/i}"
    "{i}Four small dolls sit in four small rooms. In the kitchen, a woman. In the laboratory, a tall man. In the library, a boy with a book and in the bedroom, a little girl.{/i}"
    if "b_doll" in done:
        m "{i}I am not touching the fifth doll again.{/i}"
        jump bedroom_menu
    "{i}A fifth doll lies on its side in the hall. It wears a small grey coat the same colour as yours.{/i}"
    menu:
        "What do you do?"
        "Pick up the fifth doll.":
            $ done.add("b_doll")
            $ suspicion +=  2
            "{i}It is warm. It's face is blank, unpainted and as you hold it, you feel a tiny heartbeat against your fingers.{/i}"
            "{i}Exactly in time with your own.{/i}"
            e "That one is yours."
            "{i}In shock, you set it down and hard, and the other dolls in the other rooms turn to look at you.{/i}"
            $ lore.add("b_doll")
        "Leave it lying where it is.":
            "{i}You do not touch it. In the kitchen, the tiny woman turns her head to watch you leave.{/i}"
            jump bedroom_menu
label bedroom_frame:
    "{i}There seems to be a pencil mark until nine, which maybe indicates a year of passing.{/i}"
    "'We stopped counting. She stays this tall now.'"
    if "b_frame" not in done:
        $ done.add("b_frame")
        $ lore.add("b_frame")
        m "{i}She never got any older. None of them did.{/i}"
        jump bedroom_menu
label bedroom_floorboard:
    if "o_moth" in clues:
        m "{i}I have already taken what was under that floorboard.{/i}"
        jump bedroom_menu
    "{i}At the foot of the bed, one board stays up higher than the rest. Your fingernail finds the seam, and it lifts up without a sound.{/i}"
    "{i}Underneath, you found a letter with a child's handwriting.{/i}"
    "'If you are reading this, you are in the house. I am sorry, I was first. Papa said that it would only be for a little while.'"
    "'Mama cried when she said yes.'"
    "'I do not want to be alone in the dark. I only want someone to stay.'"
    "'Be kind to us. We are all trying to be kind to it. That is how we keep it quiet.'"
    $ clues.add("o_moth")
    $ lore.add("b_letter")
    "Moth went first, then Owl and Stag and lastly, wolf of the kitchen."
    m "That is it. I figured it out."
    e "Finally, huh? Took you long enough."
    jump bedroom_menu
label backdoor_lock:
    scene black
    with fade
    "The lock is waiting for you."
    "Four carved animals stare back from the iron plate."
    "A moth, an owl, a stag and a wolf."
    "Beneath them, the thing has been scratched so much that it looks like writing."
    m "Four animals. Four rooms. Four people."
    "You place your hands against the lock."
    "It is warm."
    e "You found the way out."
    m "I just found a door. That does not mean that I trust it."
    e "You have learned so much."
    "The voice sounded like he was almost proud."
    e "You know their names. You know what they did. You know what they left behind."
    "The lock clicks just once."
    e "But do you know what you are about to open?"
    menu:
        "What do you do?"
        "Enter the orders that you discovered." if orders_found() == 4:
            jump ending_lock_attempt
        "Try to force the lock open.":
            "You grip the iron plate and pull it."
            "The lock does not move."
            "Something beneath the door pulls back."
            e "Why does everyone only try to take?"
            "Your fingers begin to hurt. You let go."
            $ suspicion += 3
            $ lock_attempts += 1
            if suspicion >= 15:
                $ caught_reason = "greed"
                jump ending_caught
            "The four animals seem quieter now."
            jump backdoor_lock
        "Try to hear what is beneath the door.":
            "You lower your hand."
            "For the first time, you stop trying to escape long enough to listen."
            "There seems to be a faint sound on the other side."
            "A child, breathing in the dark."
            fd "Are you leaving too?"
            "You could not answer immediately."
            "You then think of Mira, who is still waiting for your call that never went."
            menu:
                "What do you say?"
                "I am sorry. I should have stayed.":
                    m "I am sorry."
                    m "I should have stayed. I should have answered."
                    "The house suddenly becomes quiet."
                    e "You cannot stay for everyone."
                    m "I know."
                    "For a moment, the voice sounded less like a child and impossibly old."
                    e "Then why do you keep trying to?"
                    jump ending_stay
                "I am leaving. I cannot help you.":
                    m "I am going to leave this place. I can not help you."
                    "The silence that follows is so complete that you could hear your heartbeat at that moment."
                    e "I know."
                    "The lock turns by itself."
                    jump ending_escape
label ending_lock_attempt:
    scene black
    with dissolve 
    with fade
    "You close your eyes slowly and then try to remember."
    "The moth. The owl. The stag. The wolf."
    "You start remembering not just the animals, but the people who left them behind too."
    if "o_moth" in clues:
        "First: The moth"
    if "o_owl" in clues:
        "Second: The owl."
    if "o_stag" in clues:
        "Third: the stag"
    if "o_wolf" in clues:
        "Last: the wolf"
    "You arrange the order in your mind and then press the four marks."
    "For a moment, nothing happens."
    "Then something behind the door begins to turn."
    "One click, then another."
    "Then a sound that went on like a long, tired sigh."
    if "l_fire" in lore:
        "The lock opens."
        "But you do not pull the lock immediately."
        "You remember the burned letter in the library."
        "The thing in this house was not Lenora."
        "It had worn her loneliness like a coat. It had learned to speak in a child's voice because someone had answered it when she was afraid."
        "And the family had spent their final days trying to make it quiet."
        m "You are not her."
        "The voice at the other side says nothing."
        "You are not the little girl who wanted someone to stay."
        e "No."
        "For the first time, it does not pretend."
        e "But I was alone."
        "You think of your mother at the hospital."
        "You then think of Mara's missed calls."
        "You thought of every other time that you thought that other people had unlimited patience."
        m "I know."
        "The doors open a fraction."
        e "Will you come back?"
        "You stare at the darkness beyond the door."
        m "No."
        "You take a breath."
        m "But I will remember."
        jump ending_truth
    else:
        "The door gives you way with a slow, reluctant creak."
        "Cold air reaches your face."
        "Beyond it lies a forest, wet with rain and empty beneath the trees."
        e "You can go."
        "You hesitate a bit."
        e "You do not have to understand everything."
        e "You just simply have to leave."
        jump ending_escape
label ending_truth:
    scene black
    with fade_black
    "You step through the doorway."
    "The rain has stopped."
    "The forest stands completely still, every breath consumed by the water."
    "Behind you, the mansion which was just so huge at first is not enormous anymore."
    "It looks old and is smaller than you remember it being. The wimdows are dark and the light that you once saw outside has disappeared."
    "You turn back to look at the door for one last time."
    "it is shut."
    "You cannot feel anything's presence there, though you can faintly sense the house breathing."
    e "You know what happened there."
    m "I know some of it."
    e "The fther wanted to save his daughter."
    "A memory rises in your mind, the slow humming of the machine in the laboratory."
    e "The mother wanted her family together."
    e "The boy's only desire was that his sistor did not feel afraid."
    "You then remember the green ribbon from the boy's diary that you got."
    "The book was the boy's journal, and his care for his sister clearly was shown there by his words written in his diary."
    "The words soon had become familiar to survive even death."
    e "And Lenora..."
    "The voice falters."
    e "Lenora wanted someone to stay."
    "You stare at the mansion"
    "And you answered her."
    "The windows darken."
    e "I answered."
    m "But you were not her."
    e "No."
    "The answer is so quiet that you almost miss it."
    e "I was what she answered when she asked."
    "The wind passes through the trees."
    e "They were frightened of me. Then they were frightened of what would happen if they stopped being kind to me."
    e "They kept on giving me things."
    e "Their time."
    e "Their warmth."
    e "Their names."
    e "I learned that if i sounded lonely enough, someone would be willing to stay."
    "The word settles over you like cold dust."
    "You understand at last, why the house had welcomed you."
    "It had not mistaken you for a member of the family."
    "It had made a room for you."
    "A fifth place."
    "A fifth grave."
    "A fifth person that can be persuaded to remain."
    m "You marked my road before I was about to crash."
    e "Yes"
    m "You made me lose control."
    e "Yes"
    m "And you knew about Mira."
    e "For the first time, the voice does not answer immediately."
    e "I knew that you were waiting for someone."
    "Your stomach twists."
    "You thought you were busy enough, you would put off being needed."
    e "You thought that there would always be another call from her."
    e "You thought all the people that love you so much can tolerate you forever."
    e "Do you think acting worse just because someone can tolerate you a lot means they will just keep acting the same towards you?"
    "You look down on your phone. The screen is dark. No missed calls. No messages from Mara."
    m "I did not mean to hurt her."
    e "Neither did they."
    "You close your eyes."
    "You want to tell it that there is a difference."
    "That he did not build a machine to keep a dead child alive."
    "That you are not inviting anyone to your home."
    "That you were only tired. You were only busy. You were only human."
    "All of it is true."
    "None of it denies the fact of Mira kept calling you up."
    m "I can not undo what I did."
    e "no."
    m "But I can stop pretending that it did not matter."
    "The house at the back makes a sound like a floorboard settling, although you could not hear it from a distance."
    "You see what seemes to be a little girl's figure in the pitch black window of the bedroom, which you could not see outside of previously."
    "Then you remember the portrait where the little girl seemed to have been staring at you."
    "She was not asking you to stay, not asking you to replace her, just sking for company, only to be seen by you."
    m "I am sorry, Lenora."
    "You do not know whether the girl can even hear you or not."
    "You do not know if she is still somewhere in the house or not, and whether there is anything left of  her at all."
    "You say it anyway."
    m "I am sorry."
    "You see the light of the mansion going out."
    "One at a time, not all at once. One window, then another then the last."
    "The darkness of the house remains, but it looks like it no longer leans towards you."
    "For the first time, it looks like an empty building which has no relations with you."
    "You walk back through the forest."
    "It takes a while to reach your car, which is still bashed against the tree."
    "The steering wheel is bent and the windshield is shattered."
    "There is no way that you could have driven it home."
    "You sit beneath the tree until morning."
    scene road at bg_fit
    with dissolve
    with fade
    "When the sun rises, the forest looks pretty ordinary."
    "No mansion sits between the trees anymore."
    "There are no lights shining in the distance."
    "You do not know where the house went, if it was for a good cause or not."
    "You only know that you are alive."
    "And that means you have a lot left to do in your life."
    "You call Mira on the phone, and then she immediately answers on the third ring."
    mira "Hello?"
    mira "Where are you? I have been calling you the whole night."
    "You could make an excuse."
    "You could tell her what happened the whole night after you crashed."
    "You could begin with the easiest part. Instead, you decide to tell her the truth."
    m "I am sorry that I haven't been there."
    "Silence."
    m "I kept thinking that I could call later, visit later and then read the book with you later."
    m "I always thought that there would be a next time, i was wrong."
    mira "Are you safe?"
    m "yeah"
    mira "Then thats fine, all that it matters for now."
    m "I am coming home."
    centered "{size=+12}THE HOUSE REMEMBERS{/size}"
    centered"{i}True Ending{/i}"
    return
label ending_escape:
    scene black
    with fade_black
    "You step through the open door."
    "The rain hits your face so suddenly that you gasp."
    "For a few seconds, you cannot move."
    "You had forgotten what ordinary cold felt like."
    "Behind you, the door begins to close."
    e "wait."
    "You turn."
    "There is no figure in the doorway."
    "Only darkness."
    e "Will you come back?"
    "You stare at the gap between the door and it's frame."
    m "I don't know."
    "The answer seems to satisfy whatever that was."
    e "Nobody ever knows."
    "The door closes."
    "You hear the lock turn on the other side."
    "You just walk away from the mansion without looking back."
    "The forest is very difficult to cross. You lose your footing in the mud more than once."
    "But you just keep moving and then finally, you find the road."
    "Your car is still there broken against the tree."
    "You sit besides your car for a while until it starts to lighten."
    "When a passing driver finds you, you tell them you crashed and became lost in the forest."
    "You do not mention the mansion."
    "You do not mention the voices."
    "You do not mention the fifth grave."
    "At the hospital, the doctors tell you that you are lucky."
    "He says you have bruises, a concussion and cuts on your arms but not enough to kill you."
    "Lucky."
    "That word follows you for weeks."
    "You try to return to your ordinary life."
    "You answer your emails, attend meetings and then replace your car."
    "You tell yourself that the forest was a combination of exhaustion, alcohol and then a head injury."
    "You keep telling yourself that you never ever saw anything."
    "But on some nights, when you turn off the lights, you can hear a slow and even sound coming from somewhere in your home."
    "A wooden ball bouncing."
    "Once, twice, and then silence."
    "You never find a ball."
    "You never see the mansion again."
    "But sometimes while driving at night, you notice a light inbetween the trees."
    "You do not stop or turn around."
    "You just keep your eyes on the road."
    "Months pass before you call Mira."
    "You have rehearsed what you will say many times."
    "You have made excuses, and you have prepared explanations."
    "When she answers, you forget every one of them."
    mira "Hello?"
    m "Hey."
    mira "Are you okay? You disappeared."
    "You look at the phone in your hand."
    "You then remembered the voice in the mansion telling you how good you were at letting it ring."
    m "I am sorry."
    "The words feel small."
    "I kept thinking i would call later."
    mira "I know."
    "She sounds tired."
    mira "I just wanted to hear from you."
    "You swallow."
    m "I am here now."
    m "There is a pause."
    mira "Then stay on the phone for a bit."
    "You do."
    "You talk about ordinary things."
    "The weather, the work and the soup recipe she found."
    "Neither of you mention all the conversations you missed."
    "Neither of you can recover the time that has passed."
    "But for the first time in years, you do not look for an excuse to leave."
    "You do not know if the house is still waiting."
    "You do not know whether it has let you go, or just merely decided that you were not ready."
    "You only know that you made it out."
    "From that mansion, from that hell of a place to be in."
    "From that one place that seemed impossible to leave at one point of time, you finally left."
    "And that leaving a place is not the same as leaving everything behind."
    centered "{size =+ 12}THE ROAD HOME{/size}"
    centered "{i}ESCAPE ENDING{/i}"
    return
label ending_stay:
    scene main_hall at bg_fit
    with dissolve
    with fade
    "You do not touch the lock again."
    "Instead, you walk back to the hall."
    "The chandelier glows above you."
    "It's crystals shine bit by bit, one by one."
    "For the first time since you entered the mansion, the light does not look sickly."
    "It looks warm."
    e "You came back."
    m "I did."
    e "Everyone used to say that they were going to leave."
    m "I know."
    m "Everyone used to say that they woukd return."
    "You look at the four doors."
    "The kitchen, the laboratory, the library and the bedroom."
    "Those were the four rooms in the house. The four lives that ended before they should have."
    "And a small fifth place, prepared for someone that shoud not have belonged here."
    m "I am not one of them."
    e "no."
    m "I cannot replace Lenora."
    e "no."
    m "And I cannot make the family come back."
    "The chandelier flickers."
    e "Then what will you do?"
    "You have no answer."
    "You think about the soup that was waiting for someone to eat it on the kitchen table."
    "You think of the small ball with Lenora printed on the side."
    "You think of the boy that readstories to his sister every night so that she would not be afraid."
    "You think of the child that asked you to stay until she fell asleep."
    "You think of Mira."
    "You think of all the times you had mistaken being needed for being trapped."
    m "I can listen."
    "The house goes still."
    e "Listen?"
    m "I cannot undo what happened here."
    m "But I can listen to what happened."
    "The walls creak softly."
    e "They listened."
    m "Maybe."
    "You look towards the library."
    m "But I think that they were afraid of you."
    "For a moment, the golden light turns cold."
    e "I did not want them to go."
    m "i know."
    e "I was alone."
    m "I know."
    "The words seem to soothe it."
    "That frightens you more than the anger ever did."
    e "Then you understand."
    "You look at the empty space at the table in your memory."
    m "I understand that you were lonely."
    m "I do not understand why that means someone else has to stay."
    "A long silence follows."
    "The house seems to grow larger around you."
    "Somewhere above, the door closes."
    e "You would leave me too."
    "It sounds more like a child's accusation."
    "It sounds like something much older learning how to cry."
    "You feel the familiar urge to comfort it."
    "To promise that everything will be fine."
    "To say that you will stay as long as it takes."
    "You remember the hospital room."
    "You remember telling your mother that you would be back in two minutes."
    "You remember that she had died before you returned."
    "You remember Mira waiting for you."
    "You cannot make the same promise again."
    m "I cannot promise to stay here forever."
    "The lights dim."
    m "But I can stay tonight."
    "Something moves behind the walls."
    "Not a footstep."
    "Does not quite sound like breathing either."
    "A sound that sounded like someone was settling into bed."
    e "Tonight."
    m "Tonight."
    "The front door appears at the far end of the hall."
    "It is open."
    "Beyond it, the forest waits beneath the rain."
    "You could leave."
    "You could still leave."
    "The house does not not close the door."
    "You look at it for a long time."
    "Then you turn away."
    "You walk to the kitchen."
    "The table is set for a family that will never return."
    "You pull out the sixth chair."
    "You do not eat the soup."
    "You simply sit."
    "The steam rises from the pot."
    "For a while, there is no voice."
    "Then a small sound comes from the hallway."
    fd "Again?"
    "A wooden ball rolls into the kitchen."
    "It stops near your shoe."
    "You pick it up and roll it gently back."
    "Somewhere in the dark, something laughs."
    "You then close your eyes."
    "You tell yourself that one night is not forever."
    "You tell yourself that you can still leave in the morning."
    "Outside, the rain keeps falling."
    "And the mansion, first time in a while, does not feel quite so empty."
    "But when you look towards the open doorway again, the forest seems farther away than before."
    "You have chosen to stay."
    "You have not yet decided what the choice will cost."
    centered "{size =+ 12}A PLACE AT THE TABLE{/size}"
    centered "{i}Staying ending{/i}"
    return
label ending_caught:
    scene black
    with flicker
    "The chandelier begins to shake."
    "Every crystal rattles against the next."
    "The sound spreads through the mansion, travelling through the walls and beneath the floorboards."
    "You know that you have made a mistake."
    "You just do not know which one."
    e "You have taken so much."
    m "I was trying to get out."
    e "The ring."
    e "The book."
    e "The things that they had left for one another."
    e "The things that they wanted to keep."
    "You step back."
    "The floor seems to move beneath your feet."
    e "You touched everything."
    m "I did not know."
    e "You did not ask."
    "The walls begin to breathe."
    "The doors begin to open one by one."
    "Behind each door lies the same darkness."
    "The kitchen smells of cold soup."
    "The laboratory hums with the sound of a machine which should have been dead decades ago."
    "The library is filled with the sound of pages turning."
    "In the bedroom, a music box plays a lullaby that you remember from childhood."
    "You cover your ears."
    "The music just continues."
    e "I do not want to be angry."
    "The voice is close now."
    e "I am tired."
    m "Please."
    e "I asked them to stay."
    e "They stayed."
    e "Then they were gone."
    "Something tall stands in the far side of the hall."
    "You cannot see it's face."
    "You cannot tell whether it even has a face or not."
    "But you know that it is looking at you."
    e "I asked you too."
    "Your phone vibrates in your pocket."
    "You pull it out with shaking hands."
    "The screen lights up."
    "Mira"
    "Missed calls"
    "You try to answer."
    "Your mouth opens."
    "No sound comes out."
    mira "Why won't you ever come home?"
    m "Stop."
    e "You promised."
    m "Stop!"
    "The chandelier goes dark."
    "Something touches your shoulder."
    "It is cold and light, like the hands of a child."
    fd "Are you staying?"
    "You turn around."
    "The front door is gone."
    "The backdoor is gone."
    "The four rooms are gone."
    "Only the hall remains."
    "And at this far end, a long dining table appears."
    "Five chairs are there, and four are occupied by shapes that you cannot quite look at or perceive."
    "The fifth is empty."
    "A plate has been set in front of it."
    "A name has been written on a small card."
    "It was your name."
    m "no.."
    "You run." 
    "The hall in front of you stretches endlessly."
    "You look back."
    "The distance from the dining table has not changed one bit."
    "You run until your lung burns."
    "You run until your legs give away."
    "The fifth chair waits for you."
    e "You can rest now."
    "You try to crawl away. The floor is soft beneath your palms."
    "Not wood or stone, earth."
    "You look down, your hands are covered in dark soil."
    "There is a hole in the floor, just enough for you to fit inside, like the one you saw from the kitchen windows."
    "You remember the doll that looked exactly like you, and seemed to have a heart."
    "You remember every warning that you have ignored until now."
    "The soil begins to rise around your hands."
    "You struggle."
    "Something takes your wrist."
    "A second hand takes the other, but they are not strong."
    "They do not need to be, you are so tired."
    "You are so tired of running."
    "You think of Mira."
    "You start thinking of the calls that you never answered."
    "You try to imagine the sound of her laughter."
    "You can almost hear it."
    "Then the house itself whispers in her voice."
    mira "Come home sometime."
    "The earth reaches your shoulders."
    "You want to say that you are sorry."
    "You want to say that you were finally coming home."
    "You wanted to tell her that you never meant for this to happen."
    "But the dark fills your mouth."
    "Somewhere in the mansion, a small kid laughs."
    "The fifth chair scrapes back from the table, and an unrecognizable shape appears there as well."
    "And the house becomes quiet again."
    centered "{size =+ 12}THE FIFTH GRAVE{/size}"
    centered "{i}BAD ENDING{/i}"
    return
