#include <string>
using namespace std;

struct Order{
    enum class Side {
        BUY,
        SELL
    };
    string symbol;
    Side side;
    float quantity;
    double price;
    string timestamp;
    Order(std::string sym, Side s, int qty, double pr)
        : symbol(sym), side(s), quantity(qty), price(pr) {}
};
