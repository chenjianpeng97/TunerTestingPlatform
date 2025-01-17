import { FormItem } from '@/types/components'
import { reactive } from 'vue'
import { Message } from '@arco-design/web-vue'
import { useTable, useTableColumn } from '@/hooks/table'
const table = useTable()
export const conditionItems: Array<FormItem> = reactive([
  {
    key: 'id',
    label: 'ID',
    type: 'input',
    placeholder: '请输入通知ID',
    value: '',
    reset: function () {
      this.value = ''
    },
  },
])
export const formItems: FormItem[] = reactive([
  {
    label: '项目名称',
    key: 'project',
    value: '',
    placeholder: '请选择项目名称',
    required: true,
    type: 'select',
    validator: function () {
      if (!this.value && this.value !== '0') {
        Message.error(this.placeholder || '')
        return false
      }
      return true
    },
  },
  {
    label: '环境类型',
    key: 'environment',
    value: 0,
    type: 'select',
    required: true,
    placeholder: '请选择绑定的测试环境',
    validator: function () {
      if (!this.value && this.value !== 0) {
        Message.error(this.placeholder || '')
        return false
      }
      return true
    },
  },
  {
    label: '通知类型',
    key: 'type',
    value: 0,
    type: 'select',
    required: true,
    placeholder: '请选择通知类型',
    validator: function () {
      if (!this.value && this.value !== 0) {
        Message.error(this.placeholder || '')
        return false
      }
      return true
    },
  },
])
export const mailboxForm: FormItem[] = reactive([
  {
    label: '配置详情',
    key: 'config',
    value: '',
    type: 'select',
    required: true,
    placeholder: '请输入配置详情',
    validator: function () {
      if (this.value.length === 0) {
        Message.error(this.placeholder || '')
        return false
      }
      this.value = this.value.filter(
        (item: any) => item !== null && item !== undefined && item !== ''
      )
      this.value = JSON.stringify(this.value)
      return true
    },
  },
])
export const configForm: FormItem[] = reactive([
  {
    label: '配置详情',
    key: 'config',
    value: '',
    type: 'textarea',
    required: true,
    placeholder: '请输入配置详情',
    validator: function () {
      if (!this.value) {
        Message.error(this.placeholder || '')
        return false
      }
      return true
    },
  },
])
export const tableColumns = useTableColumn([
  table.indexColumn,
  {
    title: '项目名称',
    key: 'project',
    dataIndex: 'project',
  },
  {
    title: '对应环境',
    key: 'environment',
    dataIndex: 'test_object',
    width: 150,
  },
  {
    title: '通知类型',
    key: 'type',
    dataIndex: 'type',
    width: 150,
  },

  {
    title: '配置详情',
    key: 'config',
    dataIndex: 'config',
    align: 'left',
  },
  {
    title: '状态',
    key: 'status',
    dataIndex: 'status',
    width: 80,
  },
  {
    title: '操作',
    key: 'actions',
    dataIndex: 'actions',
    fixed: 'right',
    width: 150,
  },
])
