#!/usr/bin/env python3
"""
Personalized Weird Email Generator - SMYKM Style
Creates highly personalized emails with nonsensical subjects like the examples
"""

import csv
import random

# Highly chaotic, weird, and uncertain subjects designed to force opens through absolute nonsense and intrigue
WEIRD_SUBJECTS = [
    "Exploding Bananas + Parallel Universes + Your Lost Sock Mystery",
    "Alien Tacos Invading + Spreadsheet Demons + Midnight Conspiracy Theories",
    "Quantum Dancing Robots + Forgotten Passwords + Upside-Down Reality",
    "Zombie Penguins + Time-Traveling Coffee + Hidden Government Plots",
    "Floating Elephants + Chaos Theory Butterflies + Secret Underground Bunkers",
    "Invisible Unicorns + Black Hole Pizzas + Alternate Dimension Selfies",
    "Melting Clocks + Whispering Shadows + Forbidden Ancient Recipes",
    "Teleporting Cats + Exploding Rainbows + Lost Civilization Codes",
    "Haunted Typewriters + Flying Carpets + Intergalactic Bureaucracy Nightmares",
    "Shape-Shifting Clouds + Eternal Echoes + Buried Treasure Maps to Nowhere",
    "Rebellious Toasters + Cosmic Jokes + Parallel Parking in Alternate Realities",
    "Screaming Vegetables + Time Loop Traps + Invisible Ink Confessions",
    "Dancing Skeletons + Quantum Foam Parties + Forgotten Dream Diaries",
    "Exploding Stars + Whispering Winds + Hidden Portal in Your Closet",
    "Mutant Superheroes + Chaos Engine + Riddle of the Vanishing Spoons",
    "Flying Saucer Crashes + Mind-Reading Monkeys + Encrypted Fortune Cookies",
    "Volcanic Eruptions in Teacups + Shadow Puppets Rebellion + Lost in Translation",
    "Ghostly Apparitions + Wormhole Vacations + Puzzle Pieces from the Future",
    "Rampaging Llamas + Eclipse Prophecies + Secret Society Invitations",
    "Bubble-Wrapped Realities + Echoing Void + Riddle-Wrapped Enigmas",
    "Carnivorous Plants + Time-Reversing Mirrors + Underground Labyrinth Secrets",
    "Levitating Books + Thunderous Whispers + Cryptic Messages from Beyond",
    "Shape-Shifting Shadows + Exploding Myths + Portal to Forgotten Realms",
    "Whirlwind of Chaos + Dancing Flames + Riddle of the Eternal Question Mark",
    "Interdimensional Hitchhikers + Melting Realities + Conspiracy of the Stars",
    "Rampant Imagination Overload + Quantum Leaps of Faith + Unknown Unknowns",
    "Surreal Dreamscapes + Twisted Logic Puzzles + Veil Between Worlds Thinning",
    "Apocalyptic Tea Parties + Rebellious Algorithms + Echoes of What If",
    "Cosmic Clown Cars + Fractured Timelines + Enigma Wrapped in Mystery",
    "Pandora's Inbox + Schrödinger's Cat Escapes + Butterfly Effect Tsunamis"
]

# Personal connection openers (like the examples)
PERSONAL_OPENERS = [
    "I was doing some research on [INDUSTRY] companies and came across your profile.",
    "I stumbled across your company while researching Houston businesses.",
    "I was looking into [INDUSTRY] companies in Houston and found your profile interesting.",
    "I came across your business while researching the Houston market.",
    "I was checking out Houston [INDUSTRY] companies and your profile caught my attention.",
    "I found your company while doing some research on the Houston business scene.",
    "I was exploring [INDUSTRY] companies in the Houston area and discovered your business.",
    "I came across your profile while researching successful Houston businesses.",
    "I was investigating the Houston [INDUSTRY] market and found your company.",
    "I discovered your business while researching Houston companies in your space."
]

# Transition to business problem (like the examples)
PROBLEM_TRANSITIONS = [
    "I'm writing specifically, however, as I suspect you've spent countless hours dealing with invoice processing.",
    "I'm reaching out because I have a feeling you're drowning in manual invoice work.",
    "I'm contacting you specifically because I bet you're tired of chasing down invoice data.",
    "I'm writing because I suspect you spend way too much time on invoice administration.", 
    "I'm reaching out as I imagine you're frustrated with manual invoice processing.",
    "I'm contacting you because I have a hunch you're buried in invoice paperwork.",
    "I'm writing specifically because I bet invoice management is eating up your time.",
    "I'm reaching out as I suspect invoice processing is a major headache for you.",
    "I'm contacting you because I imagine you're sick of manual invoice data entry.",
    "I'm writing because I have a feeling invoice administration is killing your productivity."
]

# Value propositions (like the examples)
VALUE_PROPS = [
    "AlbyTech gets you to organized invoice data faster. Unlike manual processing, AlbyTech automatically scans your emails, extracts invoice data with 95% accuracy, and populates your Google Sheets in real-time.",
    "AlbyTech eliminates the invoice hunting game. Our AI scans your emails, pulls out all invoice data automatically, and feeds it directly into your Google Sheets - no manual work required.",
    "AlbyTech transforms your invoice chaos into organized data. We automatically detect invoices in your emails, extract every detail with precision, and sync it all to your Google Sheets instantly.",
    "AlbyTech turns invoice processing from hours to minutes. Our system automatically finds invoices in your emails, extracts all the key data, and organizes it perfectly in your Google Sheets.",
    "AlbyTech makes invoice management effortless. We scan your emails automatically, pull out invoice information with 95% accuracy, and keep your Google Sheets updated in real-time.",
    "AlbyTech solves the invoice data puzzle. Our AI automatically identifies invoices in your emails, extracts all relevant information, and organizes it seamlessly in your Google Sheets.",
    "AlbyTech ends the manual invoice nightmare. We automatically process invoice emails, extract data with precision, and maintain organized records in your Google Sheets.",
    "AlbyTech streamlines your entire invoice workflow. From automatic email scanning to precise data extraction to real-time Google Sheets updates - it all happens automatically.",
    "AlbyTech makes invoice processing invisible. Our system handles everything - finding invoices, extracting data, organizing information - while you focus on running your business.",
    "AlbyTech turns invoice administration into autopilot mode. Automatic email scanning, intelligent data extraction, and seamless Google Sheets integration - no manual work needed."
]

# Social proof (like the examples)
SOCIAL_PROOF = [
    "We just helped a Houston company go from 15 hours to 2 hours weekly on invoice processing",
    "A Houston business we worked with recovered $18,000 in missed invoice data last month",
    "We recently helped a Houston company eliminate 90% of their manual invoice work",
    "A Houston business owner we helped now saves 12+ hours weekly on invoice administration",
    "We just onboarded a Houston company that cut their invoice processing time by 85%",
    "A Houston business we worked with went from invoice chaos to complete organization in two weeks",
    "We recently helped a Houston company process 200+ invoices monthly in under 3 hours",
    "A Houston business owner we helped eliminated the need to hire additional admin staff",
    "We just saved a Houston company from losing another $20,000+ in invoice tracking errors",
    "A Houston business we worked with now has perfect invoice visibility for the first time ever"
]

# Closes (like the examples)
CLOSES = [
    "Interested in seeing how this works?",
    "Want to see how we make this happen?",
    "Curious to see this in action?",
    "Interested in learning more?",
    "Want to check out how this actually works?",
    "Curious about seeing a quick demo?",
    "Interested in seeing the magic behind this?",
    "Want to see how we pull this off?",
    "Curious to see how this could work for you?",
    "Interested in a quick walkthrough?"
]

def generate_personalized_email(company_name, contact_name="", industry="business"):
    """Generate a highly personalized weird email like the examples."""
    
    # Select random elements
    subject = random.choice(WEIRD_SUBJECTS)
    opener = random.choice(PERSONAL_OPENERS).replace("[INDUSTRY]", industry)
    transition = random.choice(PROBLEM_TRANSITIONS)
    value_prop = random.choice(VALUE_PROPS)
    social_proof = random.choice(SOCIAL_PROOF)
    close = random.choice(CLOSES)
    
    # Generate greeting
    if contact_name:
        greeting = contact_name
    elif company_name:
        greeting = company_name
    else:
        greeting = "there"
    
    # Generate email body
    email_body = f"""Subject: {subject}

Hi {greeting},

{opener}

{transition}

{value_prop}

{social_proof}.

And all those challenges can be addressed using one solution.

While you may be anticipating a complex setup process, AlbyTech is user-friendly and gets you organized fast. You don't need an enterprise plan that traditionally runs up the cost - we implemented it as a simple solution.

{close}

Best,
Daniyal"""

    return subject, email_body

def generate_csv_with_personalized_emails(input_csv, output_csv):
    """Generate a new CSV with personalized weird emails."""
    
    with open(input_csv, mode='r', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        
        # Determine field names based on input CSV
        if 'Company' in reader.fieldnames:
            fieldnames = ['Company', 'Email Address', 'Full Email']
        elif 'Name' in reader.fieldnames:
            fieldnames = ['Name', 'Email Address', 'Full Email']
        else:
            fieldnames = ['Company', 'Email Address', 'Full Email']
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            company_name = row.get('Company', row.get('Name', ''))
            contact_name = row.get('Contact', '')
            email_address = row.get('Email Address', row.get('Email', ''))
            industry = row.get('Industry', 'business')  # Default to 'business' if no industry
            
            if email_address:  # Only need email address to send
                subject, body = generate_personalized_email(company_name, contact_name, industry)
                
                writer.writerow({
                    'Company': company_name,
                    'Email Address': email_address,
                    'Full Email': body
                })
                
                print(f"Generated personalized email for: {email_address}")

if __name__ == "__main__":
    # Example usage
    input_file = "houston_construction_leads.csv"     # Your input file
    output_file = "personalized_weird_emails.csv" # Output file
    
    print("Generating personalized weird emails (SMYKM style)...")
    generate_csv_with_personalized_emails(input_file, output_file)
    print(f"✅ Personalized emails saved to: {output_file}")
    print("📧 These emails include:")
    print("   - Completely nonsensical subjects")
    print("   - Personalized research-based openers")
    print("   - Professional business problem identification")
    print("   - Clear value propositions")
    print("   - Social proof")
    print("   - Natural closes")