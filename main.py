def main():
    print("Welcome to the Epic Choose Your Own Adventure game!")
    print("You awaken in a mysterious forest, feeling a sense of adventure.")
    
    path_choice = input("Do you want to take the 'left' path or the 'right' path? ").lower()
    
    if path_choice == 'left':
        print("You choose the left path and come across a serene meadow.")
        meadow_choice = input("Would you like to relax in the meadow or continue exploring? (relax/explore): ").lower()
        
        if meadow_choice == 'relax':
            print("You lie down in the meadow, enjoying the warmth of the sun. The gentle breeze lulls you to sleep.")
            print("You wake up feeling refreshed, as if the meadow itself granted you energy.")
        elif meadow_choice == 'explore':
            print("You venture deeper into the meadow and find an entrance to a hidden cave.")
            cave_choice = input("Do you dare enter the cave or return to the meadow? (enter/meadow): ").lower()
            
            if cave_choice == 'enter':
                print("Inside the cave, you discover ancient writings and intricate carvings on the walls.")
                print("The cave seems to hold a history long forgotten. You leave, carrying a sense of wonder.")
            else:
                print("You decide not to enter the cave and return to the meadow, your curiosity still burning.")
        
        else:
            print("You hesitate, uncertain of your decision. The sky darkens, and a gentle rain begins to fall.")
            print("You find shelter under a large tree and wait for the rain to pass.")
    
    elif path_choice == 'right':
        print("You choose the right path and encounter a swift river cutting through the forest.")
        river_choice = input("Do you attempt to build a raft to cross or search for a bridge? (raft/bridge): ").lower()
        
        if river_choice == 'raft':
            print("You gather logs and vines, fashioning them into a sturdy raft.")
            print("Navigating the river proves challenging, but your determination prevails. You reach the other side safely.")
        elif river_choice == 'bridge':
            print("You scout the riverbank and discover a suspension bridge woven from vines and branches.")
            print("As you cross, you admire the craftsmanship and resilience of the bridge.")
        else:
            print("You stand undecided, a distant rumble of thunder urging you to make a choice.")
            print("With newfound determination, you construct a makeshift boat and navigate across, guided by instinct.")
    
    else:
        print("You stand uncertain, and nightfall envelopes the forest. The stars twinkle above as you ponder your next move.")
        print("With the morning light, you make your decision, following the path to the right.")
    
    print("As you continue your journey, you arrive at a crossroads, each path leading to a different adventure.")
    crossroads_choice = input("Will you go 'north,' 'south,' 'east,' or 'west'? ").lower()
    
    if crossroads_choice == 'north':
        print("You venture northward, stumbling upon a forgotten village nestled among the hills.")
        village_choice = input("Do you explore the village or continue your journey? (explore/continue): ").lower()
        
        if village_choice == 'explore':
            print("The village is a time capsule, its buildings and artifacts telling tales of generations past.")
            print("You spend hours exploring, feeling a connection to the past and the spirits that reside here.")
        else:
            print("With a sense of anticipation, you leave the village, excited for the new experiences that await.")
    
    elif crossroads_choice == 'south':
        print("You head south, and the landscape transforms into a dense, enchanted forest.")
        forest_choice = input("Do you follow the mystical lights deeper into the forest or blaze your own trail? (lights/trail): ").lower()
        
        if forest_choice == 'lights':
            print("You follow the lights, discovering a hidden grove where magical creatures gather.")
            print("You share stories with them, creating memories that will linger in your heart forever.")
        else:
            print("You forge your own path, facing challenges and overcoming obstacles.")
            print("Your determination and resilience make the journey worthwhile.")
    
    elif crossroads_choice == 'east':
        print("You choose the eastern path, which leads you to the edge of a breathtaking cliff overlooking the sea.")
        cliff_choice = input("Do you admire the view or dare to dive into the azure waters? (admire/dive): ").lower()
        
        if cliff_choice == 'admire':
            print("You take a moment to savor the beauty of the sea stretching before you.")
            print("The tranquility of the moment fills your soul, reminding you of the vastness of the world.")
        else:
            print("Summoning your courage, you leap from the cliff into the refreshing embrace of the ocean.")
            print("As you resurface, you feel alive and invigorated, ready for the adventures that lie ahead.")
    
    elif crossroads_choice == 'west':
        print("You journey westward and find yourself in a mystical garden, where flora and fauna coexist in harmony.")
        garden_choice = input("Will you commune with the creatures of the garden or seek wisdom from the ancient tree? (commune/wisdom): ").lower()
        
        if garden_choice == 'commune':
            print("You spend time connecting with the creatures, sharing an unspoken bond with the natural world.")
            print("The experience leaves you with a newfound appreciation for the interconnectedness of life.")
        else:
            print("You approach the ancient tree, its bark adorned with wisdom etched by generations past.")
            print("As you touch the tree, you receive insights that guide your journey and choices.")
    
    else:
        print("With a sense of adventure, you forge a path uncharted, your steps echoing in the untamed wilderness.")
        print("Each step brings new discoveries, reminding you that the journey itself is the greatest reward.")
    
    print("As your epic adventure continues, you reflect on the paths you've taken and the stories you've collected.")
    print("Remember, the choices you make shape your journey and define your destiny.")
    print("Thanks for embarking on this epic choose your own adventure!")

if __name__ == "__main__":
    main()