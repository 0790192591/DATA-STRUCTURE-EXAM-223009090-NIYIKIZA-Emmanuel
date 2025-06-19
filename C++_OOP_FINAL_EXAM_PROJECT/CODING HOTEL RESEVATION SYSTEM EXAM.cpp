#include <iostream>
#include <limits>

struct Date {
    int day, month, year;

    bool equals(const Date& other) const {
        return day == other.day && month == other.month && year == other.year;
    }
};

class RoomBase {
public:
    virtual ~RoomBase() {}
    virtual void reserve(const Date& date) = 0;
    virtual bool isReserved(const Date& date) const = 0;
    virtual void showReservations() const = 0;
};

class StandardRoom : public RoomBase {
private:
    Date* reservedDates;
    int reservedCount;

public:
    StandardRoom() : reservedDates(nullptr), reservedCount(0) {}

    ~StandardRoom() {
        delete[] reservedDates;
    }

    bool isReserved(const Date& date) const override {
        for (int i = 0; i < reservedCount; ++i) {
            if (reservedDates[i].equals(date))
                return true;
        }
        return false;
    }

    void reserve(const Date& date) override {
        if (isReserved(date)) {
            std::cout << "Standard room already reserved on "
                      << date.day << "/" << date.month << "/" << date.year << ".\n";
            return;
        }

        Date* newDates = new Date[reservedCount + 1];
        for (int i = 0; i < reservedCount; ++i)
            newDates[i] = reservedDates[i];
        newDates[reservedCount] = date;

        delete[] reservedDates;
        reservedDates = newDates;
        ++reservedCount;

        std::cout << "Standard room successfully reserved on "
                  << date.day << "/" << date.month << "/" << date.year << ".\n";
    }

    void showReservations() const override {
        for (int i = 0; i < reservedCount; ++i) {
            std::cout << "  Reserved on: "
                      << reservedDates[i].day << "/"
                      << reservedDates[i].month << "/"
                      << reservedDates[i].year << "\n";
        }
    }
};

class PremiumSuite : public RoomBase {
private:
    Date* reservedDates;
    int reservedCount;

public:
    PremiumSuite() : reservedDates(nullptr), reservedCount(0) {}

    ~PremiumSuite() {
        delete[] reservedDates;
    }

    bool isReserved(const Date& date) const override {
        for (int i = 0; i < reservedCount; ++i) {
            if (reservedDates[i].equals(date))
                return true;
        }
        return false;
    }

    void reserve(const Date& date) override {
        if (isReserved(date)) {
            std::cout << "Premium suite already reserved on "
                      << date.day << "/" << date.month << "/" << date.year << ".\n";
            return;
        }

        Date* newDates = new Date[reservedCount + 1];
        for (int i = 0; i < reservedCount; ++i)
            newDates[i] = reservedDates[i];
        newDates[reservedCount] = date;

        delete[] reservedDates;
        reservedDates = newDates;
        ++reservedCount;

        std::cout << "Premium suite successfully reserved on "
                  << date.day << "/" << date.month << "/" << date.year << ".\n";
    }

    void showReservations() const override {
        for (int i = 0; i < reservedCount; ++i) {
            std::cout << "  Reserved on: "
                      << reservedDates[i].day << "/"
                      << reservedDates[i].month << "/"
                      << reservedDates[i].year << "\n";
        }
    }
};

class Hotel {
private:
    RoomBase** rooms;
    int roomCount;

public:
    Hotel() : rooms(nullptr), roomCount(0) {}

    ~Hotel() {
        for (int i = 0; i < roomCount; ++i)
            delete rooms[i];
        delete[] rooms;
    }

    void addRoom(RoomBase* room) {
        RoomBase** newRooms = new RoomBase*[roomCount + 1];
        for (int i = 0; i < roomCount; ++i)
            newRooms[i] = rooms[i];
        newRooms[roomCount++] = room;

        delete[] rooms;
        rooms = newRooms;
        std::cout << "Room added. Total rooms: " << roomCount << "\n";
    }

    void removeRoom(int index) {
        if (index < 0 || index >= roomCount) {
            std::cout << "Invalid index.\n";
            return;
        }

        delete rooms[index];
        RoomBase** newRooms = new RoomBase*[roomCount - 1];

        for (int i = 0, j = 0; i < roomCount; ++i) {
            if (i != index)
                newRooms[j++] = rooms[i];
        }

        delete[] rooms;
        rooms = newRooms;
        --roomCount;
        std::cout << "Room removed. Total rooms: " << roomCount << "\n";
    }

    void reserveRoom(int index, const Date& date) {
        if (index < 0 || index >= roomCount) {
            std::cout << "Invalid room index.\n";
            return;
        }
        rooms[index]->reserve(date);
    }

    void listRooms() const {
        for (int i = 0; i < roomCount; ++i) {
            std::cout << "Room " << i << ": "
                      << (dynamic_cast<StandardRoom*>(rooms[i]) ? "Standard Room" : "Premium Suite")
                      << "\n";
            rooms[i]->showReservations();
        }
    }
};

void clearInput() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

int main() {
    Hotel hotel;
    int choice;

    while (true) {
        std::cout << "\n--- Hotel Reservation Menu ---\n";
        std::cout << "0. Add Standard Room\n";
        std::cout << "1. Add Premium Suite\n";
        std::cout << "2. Show Room List & Reservations\n";
        std::cout << "3. Reserve a Room\n";
        std::cout << "4. Remove Room by Index\n";
        std::cout << "5. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        if (std::cin.fail()) {
            clearInput();
            std::cout << "Invalid input. Try again.\n";
            continue;
        }

        switch (choice) {
            case 0:
                hotel.addRoom(new StandardRoom());
                break;
            case 1:
                hotel.addRoom(new PremiumSuite());
                break;
            case 2:
                hotel.listRooms();
                break;
            case 3: {
                int index;
                Date date;
                std::cout << "Enter room index: ";
                std::cin >> index;
                std::cout << "Enter reservation date (day month year): ";
                std::cin >> date.day >> date.month >> date.year;

                if (std::cin.fail()) {
                    clearInput();
                    std::cout << "Invalid input.\n";
                } else {
                    hotel.reserveRoom(index, date);
                }
                break;
            }
            case 4: {
                int index;
                std::cout << "Enter room index to remove: ";
                std::cin >> index;
                hotel.removeRoom(index);
                break;
            }
            case 5:
                std::cout << "Exiting system.\n";
                return 0;
            default:
                std::cout << "Invalid choice.\n";
        }
    }

    return 0;
}

