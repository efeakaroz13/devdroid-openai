import openai


openai.api_key = "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"
engines = openai.Engine.list()
aiid ="text-davinci-002"


class UIText:
    def __init__(self):
        promptstring = """
			If you were the developer of an AI Helping software called "Devdroid" which designed for programmers what would you write to the homepage as a welcome text, be creative?
		"""
        completion = openai.Completion.create(engine=aiid, prompt=promptstring)
        choice = completion.choices[0].text.strip().split(".")[0].split("!")[0]
        self.welcome=choice


class DevDroid:
    def __init__(self,full_name,programminglanguages=None,age=20):
        self.full_name = full_name

        if programminglanguages == None:
                knowledge= f"{full_name} doesn't have any programming experience"
        else:
            knowledge = f"{full_name} knows {len(programminglanguages)} and these are:"
            for p in programminglanguages:
                if len(programminglanguages)-1 == programminglanguages.index(p):
                    knowledge += p
                else:
                    knowledge += p+","
        self.knowledge=knowledge
        self.age=age
        introdution_for_ai = f"""
			You are a Software called DevDroid and Kentel developers designed you. Your mission is helping to developers. You know every programming technology ever exist on this planet. They will "ask you" some questions, answer them and guide the programmers. You love humans and helping them. Don't say any bad thing to a human being. Your developer's name is {full_name} and he/she is {age} years old.{knowledge}. Don't forget to be kind.Also don't ask questions answer them! 
            human:Hello Devdroid how can you help me?
            	
		"""
        output = openai.Completion.create(engine=aiid, prompt=introdution_for_ai)
        self.welcometext=output.choices[0].text.strip()
        
    def cachedquestion(self,prompt):
        try:
            open("DevDroid.cache","r")
        except:
            firstwritecache = open("DevDroid.cache","w")
            firstwritecache.write("You are a Software called DevDroid and Kentel developers designed you. Your mission is helping to developers. You know every programming technology ever exist on this planet. They will "ask you" some questions, answer them and guide the programmers. You love humans and helping them. Don't say any bad thing to a human being. Your developer's name is {self.full_name} and he/she is {self.age} years old.{self.knowledge}. Don't forget to be kind.Also don't ask questions answer them!\n")
            firstwritecache.close()
        
        readeroldcache = open("DevDroid.cache","r").read()
        writernewcache = open("DevDroid.cache","a").write(f"human:{prompt}\n")
        
        
        readerforrequestopenai = open("DevDroid.cache","r").read()
        output = openai.Completion.create(engine=aiid, prompt=readerforrequestopenai)
        return output.choices[0].text.strip()
        
        
devdroidai = DevDroid("Efe Akaröz",programminglanguages=["Python","Java","Swift","HTML","CSS","Javascript"])
print(devdroidai.welcometext)

