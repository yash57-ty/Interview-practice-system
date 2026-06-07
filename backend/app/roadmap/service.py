from app.roadmap.repository import create_roadmap,get_user_roadmaps
from app.topics.repository import get_all_topics_by_subject
from .repository import delete_user_roadmaps
def generate_roadmap(db,roadmap_data,current_user):
    delete_user_roadmaps(
        db,
        current_user.id,
        roadmap_data.subject_id
    )
     
    topics=get_all_topics_by_subject(db,roadmap_data.subject_id)
    week=1
    for topic in topics:
        create_roadmap(
            db,
            current_user.id,
            roadmap_data.subject_id,
            week,
            topic.name,
            topic.description
        )
        week+=1

    return {
    "message": "Roadmap generated successfully"}
    
def get_my_roadmaps(
    db,
    current_user
):
    return get_user_roadmaps(
        db,
        current_user.id
    )