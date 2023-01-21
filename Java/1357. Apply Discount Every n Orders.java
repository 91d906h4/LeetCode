class Cashier {
    public int n, customer;
    public double discount, price;
    public HashMap<Integer, Integer> goods = new HashMap<>();

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = ((100d - discount) / 100d);
        this.customer = 1;
        for(int i = 0; i < products.length; i++) goods.put(products[i], prices[i]);
    }
    
    public double getBill(int[] product, int[] amount) {
        price = 0.0d;

        for(int i = 0; i < product.length; i++) price += goods.get(product[i]) * amount[i];

        if(customer % n == 0) price *= discount;

        customer++;

        return (double)price;
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj.getBill(product,amount);
 */
