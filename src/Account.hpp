#pragma once
#include <string>

class Account{
  std::string IBAN_; 
  int balance_;

  public:
  Account(const std::string& IBAN, int stBalance): IBAN_(IBAN), balance_(stBalance){}
  int getBalance() const{
    return balance_;
  }
  std::string getIBAN() const{
    return IBAN_;
  }
  int changeBalance(int amount){
    return balance_ += amount;  
  }
};
