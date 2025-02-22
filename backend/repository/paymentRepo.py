from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
import database, models, schemas
from typing import List, Optional
from datetime import datetime

def get_all_payments(db: Session,
                    bill_id: Optional[int] = Query(None),
                    type: Optional[str] = Query(None)):
    all_payments=db.query(models.Payment)
    if bill_id:
       all_payments=all_payments.filter(models.Payment.bill_id==bill_id)
    if type:
        all_payments=all_payments.filter(models.Payment.type==type)
    return all_payments


# def log_to_file(message: str):
#     log_file_path = "C:\\Users\\Asim PC\\Desktop\\DB-Project\\backend\\logs\\payment_logs.txt" 
    
#     try:
#         with open(log_file_path, "a") as log_file:  # Open the file in append mode
#             current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp
#             log_file.write(f"{current_time} - {message}\n")  # Write message with timestamp
#     except Exception as e:
#         print(f"Error logging to file: {e}")


def make_payment(request:schemas.Payment, db:Session):
    try:
        new_payment= models.Payment(amount=request.amount,type=request.type,bill_id=request.bill_id)
        db.add(new_payment)
        db.commit()

    
        curr_bill = db.query(models.Bill).filter(models.Bill.id==new_payment.bill_id).first()
        curr_bill.total_amount = curr_bill.total_amount+request.amount
        db.commit()
    

        db.refresh(new_payment)
        return new_payment
    except Exception as e:
        # Rollback the transaction in case of any failure
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Close the database session
        db.close()    


def updatePayment(id: int, 
                  amount: Optional[int] = None, 
                  type: Optional[str] = None, 
                  bill_id: Optional[int] = None, 
                  db: Session = Depends):

    # Fetch the Payment record by its ID
    payment = db.query(models.Payment).filter(models.Payment.id == id).first()

    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment ID not found")   
    
    # Update the Payment fields if they are provided
    if amount is not None:
        payment.amount = amount
    if type:
        payment.type = type
    if bill_id:
        payment.bill_id = bill_id
    
    # Commit the changes to the database
    db.commit()
    db.refresh(payment)
    return payment


def deletePayment(payment_id: int, db: Session):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    
    db.delete(payment)
    db.commit()
    return {"detail": "Payment deleted successfully"}
