#include <iostream>
#include <vector>
#include <memory>

class Image {
    int w, h;
    std::vector<std::vector<bool>> image;
  public:
    Image(int w, int h) : w(w), h(h), image(h, std::vector<bool>(w)) {}
    int width() const { return w; }
    int height() const { return h; }
    void setPixel(int i, int j, bool c) {
        image[j][i] = c;
    }
    friend std::ostream& operator<<(std::ostream& os, const Image& im) {
        for (int i = 0; i < im.h; ++i) {
            for (int j = 0; j < im.w; ++j) {
                os << ".#"[im.image[i][j]];
            }
            os << '\n';
        }
        return os;
    }
};

struct Tocka {
    double x, y;
};

class Shape {
public:
    virtual ~Shape() {}
    virtual bool contains(const Tocka& t) const = 0;

    virtual Shape* clone() const = 0;

    void draw(Image& slika) const {
        int w = slika.width();
        int h = slika.height();
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (contains({i, j})) {
                    slika.setPixel(i, j, true);
                }
            }
        }
    }
};

class Pravokotnik : public Shape {
  private:
    Tocka p, q;
  public:
    Pravokotnik(const Tocka& p, const Tocka& q) : p(p), q(q) {}

    Pravokotnik* clone() const override {
        return new Pravokotnik(*this);
    }

    bool contains(const Tocka& t) const override {
        return p.x < t.x && t.x < q.x && p.y < t.y && t.y < q.y;
    }
};

class Unija : public Shape {
private:
    std::unique_ptr<Shape> prvi;
    std::unique_ptr<Shape> drugi;
public:
    Unija* clone() const override {
        return new Unija(*prvi, *drugi);
    }
    Unija(const Shape& prvi, const Shape& drugi) : prvi(prvi.clone()), drugi(drugi.clone()) {}
    bool contains(const Tocka& t) const override {
        return prvi->contains(t) || drugi->contains(t);
    }
};

void draw(Image& slika) {
    Pravokotnik p({0, 0}, {20, 15});
    Pravokotnik q({20, 10}, {26, 29});
    Unija u(p, q);
    u.draw(slika);
}

int main() {
    Image slika(30, 30);
    draw(slika);
    std::cout << slika << std::endl;
    return 0;
}
