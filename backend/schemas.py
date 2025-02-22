from pydantic import BaseModel, Field
from datetime import date,datetime
from typing import List, Optional

class UserSignUp(BaseModel):
    username: str
    email: str 
    password: str

class User(BaseModel):
    username: str
    email: str 
    password: str
    class Config:
        from_attributes = True

class updateUser(BaseModel):
    old_username : str
    new_username : Optional[str]
    new_email : Optional[str]
    new_password: Optional[str]
    class Config:
        from_attributes = True


# class Staff(BaseModel):
#     username: str
#     email: str
#     password: str
#     type: str

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    role:str = "admin"


class TokenData(BaseModel):
    username: str | None = None

class CardDetails(BaseModel):
    card_holder: str
    card_number: str
    expiry_date: str
    booking_id: int

class Admin(BaseModel):
    email: str
    password: str


class RoomCategory(BaseModel):
    type: str
    description: str
    price: int
    beds: int
    baths: int
    image: str
    size : int
    bedtype: str
    view :str
    rating: int
    capacity: int

class ShowRoomCat(RoomCategory):
    type: str
    description: str
    price: int
    beds: int
    baths: int
    image: str
    capacity: int

class Rooms(BaseModel):
    id: int
    category_id: int
    booked_status: bool

class ShowRooms(Rooms):
    category: ShowRoomCat


class roomCatPrice(BaseModel):
    id:int
    type:str
    price:int
    capacity:int
    class Config:  
        from_attributes = True    

class Booking(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_date: date
    end_date: date
  #  total_cost: int
    num_people: int

    class Config:
        from_attributes = True

class updateBooking(BaseModel):
    old_id : int        
    room_id: int
    start_date: Optional[date]
    end_date: Optional[date]
    num_people: Optional[int]

class addBill(BaseModel):
    user_id:int
    first_name:str
    last_name:str
    phone_number:str
    # total_amount:int

class makeBooking(BaseModel):
   # user_id:int
   # billInfo:addBill
    room_cat_id: int
    user_id:int
    start_date:date
    end_date:date
    total_cost: int
    num_people: int
    first_name: str
    last_name: str
    phone_number: str
    class Config:
            from_attributes = True


class checkConstraints(BaseModel):
    booking_id: int
    room_id: int
    check_in_date: date
    check_out_date: date
    class Config:
        from_attributes = True


class Payment(BaseModel):
    amount:int
    type: str
    bill_id: int

class ShowPayment(Payment):
    id:int
    class Config:
        from_attributes = True



class Manager(BaseModel):
    id:int
    name:str
    salary: int

class Staff(BaseModel):
    id:int
    name:str
    designation:str
    salary:int
    manager_id:int
    class Config:
        from_attributes = True

class Bill(BaseModel):
    id:int
    user_id:int
    total_amount:int
    first_name : str
    last_name :str
    phone_number :str


class ShowBill(Bill):
    class Config:
        from_attributes = True


class showUser(BaseModel):
    username:str
    email:str
   # first_name:Optional[str]
   # last_name: Optional[str]
   # phone_number: Optional[str]
    class Config:
        from_attributes = True

class ShowBillDetails(ShowBill):
    customer: showUser
    all_payments : List[ShowPayment]=[]
    associated_booking: Booking


class PartyHalls(BaseModel):
    id : int
    name : str
    capacity : int
    price : int
    available : bool


class Tour(BaseModel):
    id:int
    price:int
    location:str
    tour_guide_id:int

class makePartyReservation(BaseModel):
        type:str
        hall_id:int
        user_id:int
        total_amount :int
        start_time:datetime
        end_time:datetime


class makeTourReservation(BaseModel):
        tour_id:int
        user_id:int
        time:datetime    
#class addPartyReservation(BaseException):

class TourReservation(BaseModel):
    id:int
    time:datetime
    payment_id: int 
    user_id: int
    tour_id: int
    class Config:
        from_attributes = True

class showUserTourInfoAll(TourReservation):
    associated_payment: ShowPayment
    associated_tour: Tour


class PartyReservation(BaseModel):
    id:int
    type :str 
    hall_id :int
    user_id :int
    payment_id :int 
    start_time:datetime
    end_time :datetime
    class Config:
        from_attributes=True

class showUserPartyInfoAll(PartyReservation):
    associated_payment: ShowPayment
    associated_hall: PartyHalls