js_import = ('''
import { createElement as e } from 'react'
import createReactClass from 'create-react-class'
import Meow from './components/Meow'
const { div } = require('hyperscript-helpers')(e)
''')

def followingFeedComponentDidMount(self):
    if self.props.handle and len(self.props.follows):
        self.setupFeedFetch()

def followingFeedComponentDidUpdate(self, prevProps):
    if (len(self.props.follows) is not len(prevProps.follows) or
        (not prevProps.handle and self.props.handle)):
        self.setupFeedFetch()

def followingFeedSetupFeedFetch(self):
    postsBy = self.props.follows.concat([self.props.handle])
    self.props.getMyFeed(postsBy)
    self.props.getFollow(self.props.handle, 'following')
    if self.interval: clearInterval(self.interval)
    self.interval = setInterval(
        (lambda: self.props.getMyFeed(postsBy)), 2000)

def followingFeedComponentWillUnmount(self):
    if self.interval: clearInterval(self.interval)

FollowingFeed = createReactClass({
    'componentDidMount':
        lambda: followingFeedComponentDidMount(this),

    'componentDidUpdate':
        lambda prevProps: followingFeedComponentDidUpdate(this, prevProps),

    'setupFeedFetch':
        lambda: followingFeedSetupFeedFetch(this),

    'componentWillUnmount':
        lambda: followingFeedComponentWillUnmount(this),

    'render':
        lambda: div({ 'id': 'meows' },
            this.props.postList.map(lambda post: e(Meow, { 'post': post })))
    })

__pragma__('js', 'export default FollowingFeed')
