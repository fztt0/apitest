import unittest
import requests
import time

#API utilizada: REQ | RES - https://reqres.in/
url = "https://reqres.in/api/users/2"
url_user = "https://reqres.in/api/users/23"

#GET Request
response = requests.get(url)
response_user = requests.get(url_user)

#Validar o Status Code com sucesso
print(f'Status code: {response.status_code}\n')
assert response.status_code == 200

#Validar o conteúdo retornado pela API
print(f'Conteúdo retornado pela API: {response.content}\n')
assert response.content != ""

#Validar falha ao localizar user
print(f'Consulta usuário inexistente. \n Status code: {response_user.status_code}\n')
assert response_user.status_code == 404

print("Iniciando etapa de testes...")

time.sleep(2)

class TestApi(unittest.TestCase):
  def test_statuscode(self):
    self.assertEqual(response.status_code, 200)
  
  def test_content(self):
    self.assertNotEqual(response.content, '')

  def test_failstatuscode(self):
    self.assertEqual(response_user.status_code, 404)

if __name__ == '__main__':
  unittest.main()
