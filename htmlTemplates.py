css = '''
<style>
.chat-message{
   padding: 1.5rem;border-radius:0.5rem; margin-bottom:1rem; display: flex
}

.chat-message.user{
    background-color: #2D6A4F;
    color:#D8F3DC
}
.chat-message.bot{
    background-color: #40916C;
    color:#D8F3DC
}
.chat-message .avatar {
  width: 15%;
}
.chat-message .avatar img{
  width: 78px;
  height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message{
 width: 85%;
 padding: 0 1.5rem;
 color: #fff;
}
.st-emotion-cache-9ycgxx e1b2p2ww12{
colour:black;
}

'''

bot_template = '''
<div class="chat-message bot">
   <div class="avatar">
      <img src="https://images.unsplash.com/photo-1535378620166-273708d44e4c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjh8fHJvYm90fGVufDB8fDB8fHww">
      </div>
      <div class="message">{{MSG}}</div>
      </div>
'''
user_template = '''
<div class="chat-message user">
<div class="avatar">
<img src="https://images.unsplash.com/photo-1677537947200-c0c34db22a95?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODR8fGh1bWFuJTIwZmFjZXxlbnwwfHwwfHx8MA%3D%3D">
</div>
<div class="message">{{MSG}}</div>
</div>
'''
