#pragma once
#include "Account.hpp"
#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
struct TransactionEdge{
    std::string to;
    int amount;
};

class TransactionGraph{
  std::unordered_map<std::string, std::vector<TransactionEdge>> graph_;
  std::unordered_map<std::string, Account> accounts_;

  public: 
  void addTransaction(const std::string& from, const std::string& to, int amount);
  std::vector<TransactionEdge> getNeighbours();
  friend std::ostream& operator << (std::ostream& os, const TransactionGraph& gr);

};
