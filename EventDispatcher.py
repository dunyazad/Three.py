class EventDispatcher:
    def addEventListener(type, listener):
        if self._listners is None:
            self._listners = {}

        listeners = self._listners

        if listeners[type] is None:
            listeners[type] = []
        
        if listener not in listeners[type]:
            listeners[type].append(listener)

    def hasEventListener(type, listener):
        if self._listners is None:
            return False

        listeners = self._listners

        return listeners[type] is not None and listener in listeners[type]
    
    def removeEventListener(type, listener):
        if self._listners is None:
            return
        
        listeners = self._listners
        listenerArray = listeners[type]

        if listenerArray is not None:
            listenerArray.remove(listener)

    def dispatchEvent(event):
        if self._listners is None:
            return

        listeners = self._listners
        listenerArray = listeners[type]

        if listenerArray is not None:
            event.target = self

            array = copy.deepcopy(listenerArray)
            for listener in array:
                listener.call(self, event)

            event.target = None
