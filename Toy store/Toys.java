public class Toys {
    int id;
    String name;
    int quantity;
    int frequency;

    public Toys(int id, String name, int quantity, int frequency) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.frequency = frequency;
    }
    public Toys(int id, String name, int quantity) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getFrequency() {
        return frequency;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "Toy{" +
                "id=" + id +
                ", name='" + name +
                '}';
    }

}
