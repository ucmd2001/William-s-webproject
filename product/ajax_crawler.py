#抓取2021版本 Meduim.com Json文章資料
import urllib.request as req
import json
# "https://medium.com/_/graphql"
def ajax_crawler(url):
#建立一個Request物件,附加 Request.headers 的資訊
    requestData={"operationName":"TopicHandlerHomeFeed","variables":{"topicSlug":"editors-picks","feedPagingOptions":{"limit":25,"to":"1641526855932"}},"query":"query TopicHandlerHomeFeed($topicSlug: ID!, $feedPagingOptions: PagingOptions) {\n  topic(slug: $topicSlug) {\n    ...TopicHandlerHomeFeed_topic\n    __typename\n  }\n}\n\nfragment TopicHandlerHomeFeed_topic on Topic {\n  id\n  name\n  latestPosts(paging: $feedPagingOptions) {\n    postPreviews {\n      ...TopicHandlerHomeFeed_postPreview\n      __typename\n    }\n    pagingInfo {\n      next {\n        limit\n        to\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TopicHandlerHomeFeed_postPreview on PostPreview {\n  postId\n  post {\n    id\n    ...HomeFeedItem_post\n    __typename\n  }\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  ...NewsletterV3EmailToSubscribersMenuItem_post\n  __typename\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment NewsletterV3EmailToSubscribersMenuItem_post on Post {\n  id\n  creator {\n    id\n    newsletterV3 {\n      id\n      subscribersCount\n      __typename\n    }\n    __typename\n  }\n  isNewsletter\n  isAuthorNewsletter\n  __typename\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n"}
    request = req.Request(url,headers={
        "Content-Type":"application/json",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }, data=json.dumps(requestData).encode("utf-8"))


    with req.urlopen(request) as response:
        result =response.read().decode("utf-8")

    result = json.loads(result)
    items =result["data"]["topic"]["latestPosts"]["postPreviews"]
    # print(result["data"]["topic"]["latestPosts"]["postPreviews"][0]["post"]["title"])
    array=[]
    for item in items:
        element = item["post"]["title"]
        array.append(element)
        
    return array