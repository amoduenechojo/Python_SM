



phoneapps = """

        NOKIA,MAKING LIFE EASIER - EAT NG
        Press 1:For Phonebook 
        Press 2:For Messages
        Press 3:For Chat
        Press 4:For Call registers
        Press 5:For Tones
        Press 6:For Settings
        Press 7:For Call divert
        Press 8:For Games
        Press 9:For Calculator
        Press 10:For Reminders
        Press 11:For Clock
        Press 12:For Profiles
        Press 13:For Sim services
        """
print(phoneapps)

menu_option = int(input("Enter a option"))

match (menu_option):
   
    case 1:
        phonebook_menu = """
                            PHONEBOOK
                            Press 1 For Search
                            Press 2 For Service Nos
                            Press 3 For Add name
                            Press 4 For Erase
                            Press 5 For Edit
                            Press 6 For Assign tone
                            Press 7 For Send b'card
                            Press 8 For Options
                            Press 9 For Speed dial
                            Press 10 For Voice tags
                """
        print(phonebook_menu)
        phonebook_option = int(input("Enter a option"))

        match(phonebook_option):
            case 1 : print("Search")
            case 2 : print("Service Nos")
            case 3 : print("Add name")
            case 4 : print("Erase")
            case 5 : print("Edit")
            case 6 : print("Assign tone")
            case 7 : print("Send b'card'")
            case 8 : 
            
                options_menu = """
Options
Press 1 : For Type view    
Press 2 : For Memory status
"""
                print(options_menu)
                                           
                options_menu_choice = int(input("Enter a option"))
                match(options_menu_choice):
                    case 1 : print("For Type view")
                    case 2 : print("For memory status")
                            
            case 9 : print("Speed tags")
            case 10 : print("Voice tags")



    case 2: 
        messages_menu = """
                            MESSAGES
                            Press 1 To write messages
                            Press 2 Inbox
                            Press 3 Outbox
                            Press 4 Picture meesages
                            Press 5 Templates
                            Press 6 Smileys
                            Press 7 Message settings
                            Press 8 Info Service
                            Press 9 Voice mailbox number
                            Press 10 Service command editor
                """
        print(messages_menu)
        message_choice  = int(input("Enter a option"))

        match (message_choice):
            case 1 : print("To write messages")
            case 2 : print("Inbox")
            case 3 : print("Outbox")
            case 4 : print("Picture messages")
            case 5 : print("Templates")
            case 6 : print("Smileys")
            case 7 : 

                
               
                message_choice = """
Message Settings
Press 1 : Set 1
Press 2 : Common
"""
                print(message_choice)
                set_Choice  = int(input("Enter a option"))
               
                match (set_Choice):
                    case 1 :  
                        print("set_Choice ")

                        setOneOptions = """ 

Press 1 : Message centre number
Press 2 : Message sent as
Phase 3 : Message validity
"""              
                print(setOneOptions)
                set_one_Choice  = int(input("Enter a option"))
                                    
                match (set_one_Choice):
                    case 1 : print("Message centre number")  
                    case 2 : print("Message sent as")
                    case 3 : print("Message validity")
                

                    case 2 : 
                          print("Common")

                commonOptions = """                                     
Press 1 : Delivery reports
Press 2 : Reply via same centre
Phase 3 : Character support
"""
                print(commonOptions)
                set_one_Choice  = int(input("Enter a option"))
              
                match (commonChoice):
                    case 1 : print("Delivery Reports") 
                    case 2 : print("Reply via same centre")
                    case 3 : print("Character support")                     
                                                
            case 8 : print("Info service")
            case 9 : print ("Voice mailbox number")
            case 10 :print("Service command editor")

                                                   
    case 3 :print("Chat")
    case 4 : 
        print("Call register")
        call_register = """
                        CALL REGISTER
                        Press 1 For Missed calls
                        Press 2 For Received calls
                        Press 3 For Dialed numbers
                        Press 4 For Erase recent call lists
                        Press 5 To Show call duration
                        Press 6 To Show call costs
                        Press 7 For Call cost settings
                        Press 8 For Prepaid credit 
                """       
                
                             
        print(callRegister)                          
                                    
        print(show_call_durations)
        show_all_call_durations = int(input("Enter a option"))                      
                                
        match (showAllCallDurations):
            case 1 : print("Last call duration")
            case 2 : print("All calls' duration")
            case 3 : print("Received calls' duration")
            case 4 : print("Dialled calls' duration")
            case 5 : print("Clear timers")
            case 6 : 
                print("Show call costs")
                show_call_costs = """
                                    Show all costs
                                    Press 1 Last call cost
                                    Press 2 All calls' cost
                                    Press 3 Clear counters
                """
                           
        print(showCallCosts)
        show_all_call_costs = int(input("Enter a option"))
        
        match (showAllCallCosts):
           case 1 : print("Last call costs")
           case 2 : print("All calls")
           case 3 : print("Clear counters")

    case 7 : 
        print("Call cost settings")
        call_cost_settings = """
            Call costs settings
            Press 1 Call cost limit
            Press 2 Show costs in
          
                """
        print(callCostSettings)
        list_call_cost_settings = int(input("Enter a option"))
        match (listCallCostSettings):
                case 1 : print("call cost limit")
                case 2 : print("show costs in")             
                                                                
                                                
    case 8 : print("Prepaid credit")

    case 5: 
        print("Tones")
        tones = """
                TONES
                Press 1 For Ringing tone
                Press 2 For Ringing volume
                Press 3 For Incoming call alert
                Press 4 For Composer
                Press 5 For Message alert tone
                Press 6 For Keypad tones
                Press 7 For Warning and game tones
                Press 8 For Vibrating alert
                Press 9 For Screen saver
                """ 
        print(tones)
        chooseTones = int(input("Enter a option"))
        match (chooseTones):
          case 1 : print("Ringing tone")
          case 2 : print("Ringing volume")
          case 3 : print("Incoming call alert")
          case 4 : print("Composer")
          case 5 : print("Message alert tone")
          case 6 : print("Keypad tones")
          case 7 : print("Warning and game tone")
          case 8 : print("Vibrating alert")
          case 9 : print("Screen saver")  
    
    case 6:
        print("Settings")
        settings = """
                 SETTINGS
                    Press 1 : Call settings 
                    Press 2 : Phone settings   
                    Press 3 : Security settings
                    Press 3 : Restore factory settings
                    """
        print(settings)
        chooseSettings = int(input("Enter a option"))
        match (chooseSettings):
            case 1 :
              print("Call settings")
              callSettings = """
                             CALL SETTINGS
                                Press 1 : Automatic redial 
                                Press 2 : Speed dialling
                                Press 3 : Call waiting options
                                Press 4 : Own number ending
                                Press 5 : Phone line in use 
                                Press 6 : Automatic answer
                     """    
              print(callSettings)
              call_settings_choice = int(input("Enter a option"))
              match (callSettingsChoice):
                case 1 : print("Automatic redial")
                case 2 : print("Speed dialling")
                case 3 : print("Call waiting options")
                case 4 : print("Own number ending")
                case 5 : print("Phone line in use")
                case 6 : print ("Automatic answer")

            case 2 : 
              print("Phone settings")
              phoneSettings = """
                             PHONE SETTINGS
                             Press 1 : Language
                             Press 2 : Call info display
                             Press 3 : Welcome note
                             Press 4: Network selection 
                             Press 5 : Lights
                             Press 6 : Confirm SIM service actions
                    """     
              print(phoneSettings)
              phoneSettingsChoice = int(input("Enter a option"))
              match (phoneSettingsChoice):
                case 1 : print("Language")
                case 2 : print("Cell info display")
                case 3 : print("Welcome note")
                case 4 : print("Network selection")
                case 5 : print("Lights")
                case 6 : print ("Confirm SIM service answer")

            case 3 : 
                print("Security settings")                                    
                securitySettings = """
                                             SECURITY SETTINGS
                                             Press 1 : Pin code request
                                             Press 2 : Cell barring service
                                             Press 3 : Fixed dialling
                                             Press 4: Closed user group 
                                             Press 5 : Phone settings
                                             Press 6 : Change access codes 
                    """
                print(securitySettings)
                SecuritySettingsChoice = int(input("Enter a option"))
                match (securitySettingsChoice):                         
                    case 1 : print("PIN code request")
                    case 2 : print("Call barring service")
                    case 3 : print("Fixed dialling")
                    case 4 : print("Closed use group")
                    case 5 : print("Phone security")
                    case 6 : print ("Change access codes")
                    case 7 : print("Call divert")
                    case 8 : print("Games")
                    case 9 : print("Calculator")
                    case 10 : print("Reminders")
                    case 11:
                        print("Clock")
                        clock = """
                                     CLOCK
                                     Press 1 : Alarm clock
                                     Press 2 : Clock settings
                                     Press 3 : Date setting
                                     Press 4: Stopwatch  
                                     Press 5 : Countdown timer
                                     Press 6 : Auto update of date and time     
                    """
                print(clock)
                clockSettings = int(input("Enter a option"))
                match (clockSettings):
                    case 1 : print ("Alarm clock")
                    case 2 : print ("Clock settings")
                    case 3 : print ("Stopwatch")
                    case 4 : print ("Countdown timer")
                    case 5 : print ("Auto update time and date")

                       
    case 12 : print("Profiles")
    case 13 : print("SIM services")
            
