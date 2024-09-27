from app.domain.entities.post import Post
from app.domain.repositories.post_repository import PostRepository

class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def create_post(self, title: str, content: str, user_id: int):
        post = Post(id=None, title=title, content=content, user_id=user_id)
        self.post_repository.add(post)
        return post

    def get_post(self, post_id: int) -> Post:
        return self.post_repository.get_by_id(post_id)
