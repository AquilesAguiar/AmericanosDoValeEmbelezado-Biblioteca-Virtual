import json
import hashlib

def adicionarUser(nome,email,senha):
    with open("src\\database\\users.json", encoding='utf-8') as js:

        users = json.load(js)
        
        for user in users:
            if user['email'] == email:
                return False
        hash = hashlib.sha512(str(senha).encode('utf-8')).hexdigest()
        users.append(
            {
                "nome":nome,
                "email":email,
                "senha":hash
            }
        )
        usersNovo = json.dumps(users)

        jsonFile = open('src\\database\\users.json', "w")
        jsonFile.write(usersNovo)
        jsonFile.close()
        return True

def logarUsuario(email,senha):
    hash = hashlib.sha512(str(senha).encode('utf-8')).hexdigest()
    with open('src\\database\\users.json', encoding='utf-8') as js:

        users = json.load(js)
        
        for user in users:
            if user['email'] == email and user['senha'] == hash:
                return True

        return False

def dadosUser(email,senha):
    hash = hashlib.sha512(str(senha).encode('utf-8')).hexdigest()
    with open('src\\database\\users.json', encoding='utf-8') as js:
        
        users = json.load(js)
        
        for user in users:
            if user['email'] == email and user['senha'] == hash:
                return user
