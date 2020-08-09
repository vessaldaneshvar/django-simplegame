from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from hashlib import sha256
import json
import uuid
class RockConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        if self.group_name in self.channel_layer.groups.keys():
            if len(self.channel_layer.groups[self.group_name]) == 2:
                print(self.channel_layer.groups[self.group_name])
                print(self.group_name)
                self.close()
            else:
                self.accept()
                async_to_sync(self.channel_layer.group_add)(
                    self.group_name,
                    self.channel_name
                )
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {'type':'start_game'}
                )
        else:
            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )
        self.close()
    
    def receive(self,text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {'type' : 'game_play','text_data':text_data,'channel_name':self.channel_name}
        )
    def start_game(self,event):
        self.send(json.dumps({'type':'initiated_game','players':self.channel_layer.groups[self.group_name],'you':self.channel_name}))

    def game_play(self,event):
        channel_name = event["channel_name"]
        text_data = event["text_data"]
        self.send(json.dumps({
            'type':'game_play',
            channel_name:text_data,
            
        }))

class DotsConsumerInit(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        if self.group_name in self.channel_layer.groups.keys():
            if len(self.channel_layer.groups[self.group_name]) == 2:
                print(self.channel_layer.groups[self.group_name])
                print(self.group_name)
                self.close()
            else:
                self.accept()
                async_to_sync(self.channel_layer.group_add)(
                    self.group_name,
                    self.channel_name
                )
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {'type':'start_game'}
                )
        else:
            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )
        self.close()
            

    def start_game(self,event):
        self.send(json.dumps({
            'type':'initiated_game',
            'secret_group_name':sha256(f'{self.group_name}+123'.encode()).hexdigest(),
            'player':list(self.channel_layer.groups[self.group_name].keys()).index(self.channel_name)+1
            }))

class DotsConsumerGame(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['secretgroupname']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        self.close()

    def receive(self,text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'start':
            self.player = text_data_json['player']
        elif text_data_json['type'] == 'action':
            if text_data_json['player'] != self.player:
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {'type' : 'game_action',"location":text_data_json['location'],'orientation':text_data_json["orientation"],'channel_name':self.channel_name}
                )

    def game_action(self,event):
        if self.channel_name != event["channel_name"]:
            self.send(json.dumps({
                'type' : 'action',
                'location' : event['location'],
                'orientation' : event['orientation']
            }))
