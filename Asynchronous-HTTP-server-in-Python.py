#updated code
import tornado.ioloop
import tornado.web
import httplib2
import concurrent.futures

class AsyncHandler(tornado.web.RequestHandler):
    async def get(self):
        http = httplib2.Http()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            self.response, self.content = await http.request("http://ip.jsontest.com/", "GET")
        self._async_callback(self.response, self.content)

    def _async_callback(self, response, content):
        print("Content:", content)
        print("Response:\nStatusCode: %s Location: %s"
              % (response['status'], response['content-location']))
        self.finish()
        tornado.ioloop.IOLoop.current().stop()

application = tornado.web.Application([
    (r"/", AsyncHandler)
], debug=True)

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()





"""
#outdated code

import tornado.ioloop
import tornado.web
import httplib2

class AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http=httplib2.Http()
        self.response,self.response=http.request('https://ip.jsontest.com','GET')
        self._async_callback(self.response,self.content )
            
    def __async__callback(self,response,content):
        print('Content:',content)
        print("Response:\nStatusCode: %s Location: %s" %(response['status'],response['content-location']))
        self.finish()
        tornado.ioloop.IOloop.instance().stop()
application=tornado.web.Application([(r'/',AsyncHandler)], debug = True)


if __name__ =='__name__':
    application.listen(888)
    tornado.ioloop.IOLoop.instance.start()
    
"""
    