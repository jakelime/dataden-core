from django.shortcuts import render

from main.dbutils import get_db_handle


# Create your views here.
def hello_world_view(request):
    """
    Renders the hello_world.html template.
    """
    db, _ = get_db_handle()
    collection_name = db["medicinedetails"]
    medicine_1 = {
        "medicine_id": "RR000123456",
        "common_name": "Paracetamol",
        "scientific_name": "",
        "available": "Y",
        "category": "fever",
    }
    medicine_2 = {
        "medicine_id": "RR000342522",
        "common_name": "Metformin",
        "scientific_name": "",
        "available": "Y",
        "category": "type 2 diabetes",
    }
    # Insert the documents
    collection_name.insert_many([medicine_1, medicine_2])
    # Check the count
    count = collection_name.count_documents({})
    # Read the documents
    med_details_cursor = collection_name.find({})  # Keep it as a cursor or list
    med_details_list = [r["common_name"] for r in med_details_cursor]  # Get the names
    # Join with actual newline characters
    med_details_string = "\n".join(med_details_list)
    context = {"message": f"medicine count={count}\n{med_details_string}"}

    return render(request, "gmailreader/hello.html", context)


#TODO:
# Stopped at hello world
# to create trigger to call gmailreader