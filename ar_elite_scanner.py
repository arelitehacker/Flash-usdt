import os
from web3 import Web3
from colorama import Fore, Style

# Jani's Professional Setup
class ArEliteScanner:
    def __init__(self, provider_url):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.tag = f"{Fore.CYAN}🔱 [JANI-SCANNER]{Style.RESET_ALL}"

    def connect(self):
        if self.w3.is_connected():
            print(f"{self.tag} Connection Successful, Jani! System Online.")
        else:
            print(f"{self.tag} Connection Failed. Check your Infura/Alchemy URL.")

    def get_wallet_info(self, address):
        try:
            # Check balance in Ether
            balance = self.w3.eth.get_balance(address)
            eth_balance = self.w3.from_wei(balance, 'ether')
            # Check transaction count (Nonce)
            tx_count = self.w3.eth.get_transaction_count(address)
            
            print(f"\n{Fore.GREEN}--- Wallet Data for: {address} ---{Style.RESET_ALL}")
            print(f"💰 Balance: {eth_balance} ETH")
            print(f"🔢 Transactions: {tx_count}")
        except Exception as e:
            print(f"{self.tag} Error: {e}")

# Usage
if __name__ == "__main__":
    # Yahan apni Infura ya Alchemy API key lagao
    API_URL = "https://sepolia.infura.io/v3/YOUR_PROJECT_ID"
    scanner = ArEliteScanner(API_URL)
    scanner.connect()
    
    # Test address (Vitalik's address as example)
    target_wallet = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    scanner.get_wallet_info(target_wallet)
