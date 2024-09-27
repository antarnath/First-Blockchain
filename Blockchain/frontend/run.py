from flask import Flask, render_template, request, redirect, url_for
from Blockchain.client.sentBTC import SendBTC


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def wallet():
  message = ''
  if request.method == 'POST':
    FromAddress = request.form.get('fromAddress')
    ToAddress = request.form.get('toAddress')
    Amount = request.form.get('Amount', type = int)
    sendCoin = SendBTC(FromAddress, ToAddress, Amount)
    if not sendCoin.prepareTransaction():
      message = "Insufficient Balance"
  return render_template('wallet.html', message = message)

def main(utxos):
  global UTXOS
  UTXOS = utxos
  app.run()