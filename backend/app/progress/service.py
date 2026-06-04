from .repository import get_progress_by_user,create_progress


def create_user_progress(
    db,progress_data,current_user):

    percentage = (
        progress_data.completed_topics * 100
    ) // progress_data.total_topics

    return create_progress(
        db,
        current_user.id,
        progress_data.subject_id,
        progress_data.completed_topics,
        progress_data.total_topics,
        percentage
    )

def get_user_progress(
    db,
    current_user
):
    return get_progress_by_user(
        db,
        current_user.id
    )