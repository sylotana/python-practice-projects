from datetime import datetime, timezone
from fastapi import FastAPI, Body, Header, Response
from model import Tag, TagIn, TagOut

app = FastAPI()


@app.post("/")
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(timezone.utc))
    return tag_in
