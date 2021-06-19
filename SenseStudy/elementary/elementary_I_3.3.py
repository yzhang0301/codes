ts = get_visualizer()
imgs_a = load_image_folder('albert')
imgs_b = load_image_folder('bruce')
imgs_c = load_image_folder('chadwick')
imgs_d = load_image_folder('diana')

for item in imgs_a:
    feature = get_face_feature(item)
    add_image(ts, item, feature, "albert")
for item in imgs_b:
    feature = get_face_feature(item)
    add_image(ts, item, feature, "bruce")
for item in imgs_c:
    feature = get_face_feature(item)
    add_image(ts, item, feature, "chadwick")
for item in imgs_d:
    feature = get_face_feature(item)
    add_image(ts, item, feature, "diana")

fit_transform(ts)
scatters = visualize_points(ts)
show_visualize(ts, scatters)
visualize_image(ts)
