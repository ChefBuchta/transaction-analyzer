#pragma once
#include <string>

class Account{
  std::string IBAN_; 
  int balance_;

  public:
  Account(const std::string& IBAN, int stBalance);
  int getBalance() const;
  int getIBAN() const;
  int changeBalance(int amount); 
};
