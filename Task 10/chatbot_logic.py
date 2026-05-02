def get_bot_response(text):
    # Knowledge Base
    responses = {
     "university": "Superior University",
     "admission_fee": "The one-time admission fee at Superior University is approximately 20,000 PKR.",
     "tuition_fee": "At Superior University, tuition charges vary depending on the selected program and semester level.",
     "starting_fee": "Most programs at Superior University start with an average fee of about 50,000 PKR per semester.",
     "bscs_fee": "The BS Computer Science program at Superior University costs around 50,000 PKR per semester.",
     "it_fee": "The Information Technology program at Superior University has an estimated fee of 45,000 PKR per semester.",
     "se_fee": "Students enrolled in Software Engineering at Superior University pay roughly 55,000 PKR per semester.",
     "bba_fee": "The Business Administration program at Superior University is about 40,000 PKR per semester.",
     "ai_fee": "The Artificial Intelligence program at Superior University charges approximately 60,000 PKR per semester.",
     "application_fee": "Applicants to Superior University are required to pay a nominal processing fee when submitting their application.",
     "deadline": "The application deadline for Superior University is 30th August.",
     "admission_start": "Admissions at Superior University usually begin in July each year.",
     "late_application": "Late applications at Superior University may be considered with an additional fee.",
     "programs": "Superior University offers programs in Computer Science, IT, Software Engineering, Business Administration, and Artificial Intelligence.",
     "bscs_availability": "Yes, Superior University offers a BS Computer Science degree.",
     "se_availability": "Software Engineering is available as a full degree program at Superior University.",
     "business_availability": "Superior University also offers a Business Administration program.",

     "eligibility": "Admission criteria at Superior University typically require at least 50% marks in intermediate, depending on the program.",
     "low_marks": "Applicants with less than 50% marks are generally not eligible for admission at Superior University.",
     "qualification": "Candidates must have completed intermediate education or an equivalent qualification to apply to Superior University.",
     "minimum_marks": "A minimum of 50% marks is required for most programs at Superior University.",
     "olevels": "Superior University accepts O-Level qualifications after equivalency conversion.",

     "entry_test": "Superior University requires an entry test as part of its admission process.",
     "entry_test_passing": "Students must secure at least 50% marks to pass the entry test at Superior University.",
     "entry_test_required": "The entry test is compulsory for admission to Superior University.",

     "scholarship": "Superior University offers merit-based scholarships to outstanding students.",
     "scholarship_apply": "Students can apply for scholarships during the admission process at Superior University.",
     "need_based": "Need-based financial assistance is also available at Superior University.",

     "hostel": "Superior University provides hostel accommodation for its students.",
     "hostel_fee": "Hostel fees at Superior University depend on the room type and facilities.",
     "girls_hostel": "Separate hostel facilities are available for female students at Superior University.",

     "documents": "Applicants must submit CNIC/B-Form, photographs, and academic certificates to Superior University.",
     "original_docs": "Original documents are required for verification at Superior University.",
     "document_submission": "All required documents must be submitted at the time of admission to Superior University.",

     "classes_start": "Classes at Superior University typically begin in September.",
     "timing": "At Superior University, classes are conducted in both morning and afternoon shifts.",
     "weekend": "Superior University offers weekend classes for selected programs.",

     "installments": "Superior University allows students to pay their fees in installments.",
     "late_fee": "Late fee payments at Superior University will result in additional charges.",
     "refund": "Fee refunds at Superior University are processed according to university policies."
     }

    # Match keywords
    for key in responses:
        if key in text:
            return responses[key]
            
    return "I'm sorry, I don't have information on that. Please try asking about admissions, deadlines, or programs."
