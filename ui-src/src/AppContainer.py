js_import = ('''
import { connect } from 'react-redux'
import App from './App'
import { logOut, resetState, getFirstName, appProperty, getHandle, getHandles, getFollow, getPostsBy, getProfilePic } from './actions'
''')

mapStateToProps = lambda state: __pragma__('js', '{}', '{ ...state }')

mapDispatchToProps = lambda dispatch: {
    'logOut': lambda: dispatch(
        logOut()),

    'resetState': lambda: dispatch(
        resetState()),

    'getFirstName': lambda: dispatch(
        getFirstName()),

    'getMyHandle': lambda: dispatch(
        appProperty('Agent_Handle')),

    'getHandle': lambda userHash, isMe, then: dispatch(
        getHandle(userHash, isMe, then)),

    'getHandles': lambda then: dispatch(
        getHandles(then)),

    'getFollow': lambda handle, type, then: dispatch(
        getFollow(handle, type, then)),

    'getPostsBy': lambda handles, then: dispatch(
        getPostsBy(handles, then)),

    'getProfilePic': lambda: dispatch(
        getProfilePic())
    }

__pragma__('js', 'export default connect(mapStateToProps, mapDispatchToProps)(App)')
